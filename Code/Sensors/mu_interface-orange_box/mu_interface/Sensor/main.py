#!/usr/bin/env python3
import sys
import socket
import logging
import argparse
import serial
import time
from pathlib import Path

from sensor_node import Sensor_Node
from mu_interface.Utilities.log_formatter import setup_logger


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments for the sensor node.")
    parser.add_argument('--port', action='store', default='/dev/ttyACM0',
        help="Port where the measurement unit is connected.")
    parser.add_argument('--baud', action='store', type=int, default=460800,
        help="Baudrate for communicating with the measurement unit.")
    parser.add_argument('--baud2', action='store', type=int, default=115200,
        help="Backup baudrate if the main one fails.")
    parser.add_argument('--int', action='store', type=int, default=10000,
        help="Time interval between two measurements (in miliseconds).")
    parser.add_argument('--addr', action='store', default='localhost',
        help="Address of the MQTT subscriber. Can be IP, localhost, *.local, etc.")
    parser.add_argument('--dir', action='store', default=Path.home() / 'measurements',
        help="Directory where measurement data is saved.")
    parser.add_argument('--multi', action='store_true',
        help="Flag specifying that multiple MU sensors are connected to one sensor node.")
    parser.add_argument('--debug', action='store_true',
        help="Flag to enable debug messages.")
    args = parser.parse_args()

    port_id = args.port.split("/")[-1]

    if args.addr == "localhost":
        hostname = port_id
    elif args.multi:
        hostname = f"{socket.gethostname()}_" + port_id
    else:
        hostname = socket.gethostname()

    #with open(Path.home() / "OrangeBox/status/experiment_number.txt", "r") as f:
    #    experiment_number = int(f.read())
    #experiment_name = f"{socket.gethostname()}_{experiment_number}"

    csv_dir = Path(args.dir)
    #csv_dir = csv_dir / experiment_name / "MU"
    if args.multi:
        csv_dir /= port_id

    #file_prefix = f"{experiment_name}_{port_id}"

    setup_logger(hostname, level=logging.DEBUG if args.debug else logging.INFO)
    logging.info("Starting sensor node.")

    baud = args.baud

    connected = False
    while True:
        while not connected:
            try:
                SN = Sensor_Node(hostname, args.port, baud, args.int, args.addr, csv_dir, "ACM0")
                connected = True
                logging.info("Connected!")
            except serial.serialutil.SerialException as e:
                print("Waiting for connection...", e)
            time.sleep(5.0)

        try:
            SN.check()
            SN.start()
        # User interrupted the program with Ctrl-C.
        except KeyboardInterrupt:
            logging.warning("Interrupted! Wait for the program to exit.")
            SN.stop()
            time.sleep(1.0)
            SN.shutdown()
            time.sleep(5.0)
            sys.exit(0)
        # There was a timeout while writing or reading from the device.
        except serial.serialutil.SerialTimeoutException as e:
            logging.error(f"Device not responding! - {e}")
            connected = False
            time.sleep(5.0)
            SN.close()
            # HACK: For some mysterious reason, opening the port with different baud rate unblocks the communication.
            if baud == args.baud:
                baud = args.baud2
            else:
                baud = args.baud
            time.sleep(1.0)
        # Device got disconnected or serial port is not available.
        except (serial.serialutil.PortNotOpenError, serial.serialutil.SerialException):
            logging.error("Device disconnected!")
            connected = False
            time.sleep(1.0)
            SN.close()
            time.sleep(1.0)
