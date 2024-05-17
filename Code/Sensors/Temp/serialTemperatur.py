import serial
from datetime import datetime
import csv
import os
import glob


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


directory = '/home/pi/Measurements/'  # directory to store the data in
last_csv_time = datetime.now()   # get the starting temperature

if not os.path.exists(directory):
    os.makedirs(directory)

serial_ports = glob.glob("/dev/ttyACM3")  # finding all serial ports with the name /dev/ttyACM

serial_instances = {}  # storing the serial instances

for port in serial_ports:
    ser = serial.Serial(port, 19200, timeout=1)
    ser.flushInput()  # Clear any existing data in the input buffer
    serial_instances[port] = ser  # add the port as an instance

header = ["timestamp", "T1_leaf", "T2_leaf", "T1_air", "T2_air"]  # headers for the csv file
start_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

while True:  # loop to read the data from the ports

    for port, ser in serial_instances.items():
        ser_bytes = ser.readline()
        # ser_bytes = ser_bytes.decode().strip()  # Convert bytes to string and remove leading/trailing whitespace
        try:  # checking the format of the incoming data
            if (ser_bytes[0] != 80 and ser_bytes[-1] != "#") or len(ser_bytes) == 0 or len(ser_bytes) != 11:  # *P3#
                continue
        except Exception as e:
            continue

        file_prefix = chr(ser_bytes[0]) + str(ser_bytes[1])
        print(file_prefix)
        T1 = ser_bytes[2] + ser_bytes[3]/10
        T2 = ser_bytes[4] + ser_bytes[5] / 10
        T3 = ser_bytes[6] + ser_bytes[7] / 10
        T4 = ser_bytes[8] + ser_bytes[9] / 10
        print(T1, T2, T3, T4)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

        Specific_directory = directory + file_prefix

        current_time = datetime.now()
        if current_time.hour in {0, 14} and current_time.hour != last_csv_time.hour:  # create new file every 12 hours
            last_csv_time = datetime.now()
            start_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
            file_path = os.path.join(Specific_directory, f'{file_prefix}_{start_timestamp}.csv')
            print("new file: ", start_timestamp)

        if not os.path.exists(Specific_directory):
            os.makedirs(Specific_directory)

        file_path = os.path.join(Specific_directory, f'{file_prefix}_{start_timestamp}.csv')
        # print(serial_instances)

        with open(file_path, "a") as f:  # writing the csv file
            writer = csv.writer(f, delimiter=",")

            if os.path.getsize(file_path) == 0:  # for empty files write the header row
                writer.writerow(header)

            writer.writerow([timestamp, T1, T2, T3, T4])  # Write the data row containing timestamp, data, and a "0" for the "filtered" value