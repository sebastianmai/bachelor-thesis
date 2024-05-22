#!/usr/bin/env python3
import logging
import re
import time

import serial


class WatchdogCounter:
    def __init__(self, timeout_multiplier, timeout_value):
        self.timeout_multiplier = timeout_multiplier
        self.timeout_value = timeout_value
        self.limit = 0
        self.update_limit(timeout_value)
        self.last_valid = None

    def check(self, data, target):
        if self.last_valid is None:
            self.last_valid = time.time()

        # Compare received data with target data using regex
        if re.match(target, data):
            self.last_valid = time.time()

        delay = time.time() - self.last_valid
        relative_delay = round(delay / self.timeout_value, 1)

        if delay >= self.limit:
            return False, relative_delay

        return True, relative_delay

    def update_limit(self, timeout_value):
        self.timeout_value = timeout_value
        self.limit = self.timeout_multiplier * timeout_value


class Cybres_MU:
    def __init__(self, port_name, baudrate=460800):
        self.timeout = 1

        self.ser = serial.Serial(
            port=None,
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=self.timeout,
            write_timeout=self.timeout,
            xonxoff=False,
            rtscts=True,
            dsrdtr=False,
        )

        self.data_watchdog = WatchdogCounter(3, 10)
        self.frame_watchdog = WatchdogCounter(3, 10)

        self.ser.port = port_name
        self.ser.rts = True
        self.ser.dtr = False
        time.sleep(0.1)
        self.ser.open()
        time.sleep(0.1)

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()  # Just in case...

        time.sleep(0.1)
        # self.ser.close()
        # time.sleep(0.1)
        # self.ser.open()
        # time.sleep(0.1)

        self.start_char = "Z"

    # Finds the start of the next data set
    def find_start(self):
        start_found = False
        while not start_found:
            # If serial buffer is empty, read will return an empty string after timeout.
            char = self.ser.read(1).decode("ascii")

            # Check that we are receiving something.
            ok, delay = self.data_watchdog.check(char, r".+")
            if not ok:
                logging.error(
                    f"Nothing received from Blue box {delay} times longer than expected."
                )
            ok, delay = self.frame_watchdog.check(char, r"A")
            if not ok:
                logging.error(
                    f"Start char not found {delay} times longer than expected."
                )

            if char == "A":
                start_found = True
        self.start_char = char

    # Returns the next complete data set
    def get_next(self):
        line = ""
        end_found = False
        if self.start_char != "A":
            self.find_start()
        while not end_found:
            next_char = self.ser.read(1).decode("ascii")
            ok, delay = self.frame_watchdog.check(next_char, r"Z")
            if not ok:
                logging.error(
                    f"End char not found {delay} times longer than expected.",
                )

            if next_char == "Z":
                end_found = True
            else:
                line += next_char
            self.start_char = next_char
        return line[:-1]

    def get_initial_status(self):
        self.ser.write(b",ss*")
        return self._get_response(sleep_time=0.5)

    def restart(self):
        self.ser.write(b",sr*")

    def start_measurement(self):
        self.ser.write(b",ms*")

    def stop_measurement(self):
        self.ser.write(b",mp*")

    def set_eis(self):
        # self.ser.write(b",y11")                  # TIA amplification gain
        self.ser.write(b",yw2*")                   # 3 - single channel, 2 - both channel
        self.ser.write(b",mt4*")
        # Allows to set the measurement mode
        # 0 - Off
        # 1 - Impedance spectroscopy (Allows for upper and lower limit to be set)
        # 5 - FRP (10 Hz- 120 kHz)
        # 6 - continuous FRP (10 Hz to 450 Hz)
        self.ser.write(b",yn3*")

        self.ser.write(b",yl004500*")              # lower bound frequency needs 6 digits else error
        self.ser.write(b",yr0000100*")             # step frequency taken  needs 7 digits else error
        self.ser.write(b",yh010000*")              # upper bound frequency needs 6 digits else error
        # self.ser.write(b", yy1*")                 # set waveform Signal Range
        # self.ser.write(b", ys00")                 # sets Waveform Type
        return self._get_response(sleep_time=0.5)

    def set_measurement_interval(self, interval):
        self.data_watchdog.update_limit(interval / 1000)
        self.frame_watchdog.update_limit(interval / 1000)

        set_interval = ",mi{:05}*".format(interval)
        self.ser.write(set_interval.encode())
        return self._get_response(sleep_time=0.5)

    def to_flash(self):
        self.ser.write(b"sf2*")

    def read_all_lines(self):
        self.ser.write(b"f1*")  # f1, mr
        while True:
            line = self.get_next()
            print(line)

    # def read_all(self):
    #     self.ser.write(b'f1*')
    #     counter = 0
    #     while True:
    #         char = self.return_serial()
    #         print(char, end='')
    #         if char == 'A':
    #             counter +=1
    #             print(f"-----------------{counter}---------------------------")

    def _get_response(self, sleep_time=0.1):
        time.sleep(sleep_time)
        response = ""
        while self.ser.in_waiting:
            response += self.ser.read(1).decode("ascii")
        return response


def test_mu():
    mu = Cybres_MU("/dev/ttyACM1")
    mu.set_measurement_interval(1000)
    mu.to_flash()
    mu.start_measurement()
    time.sleep(180)
    print("Now reading")
    # mu.read_all()


def test_watchdog():
    watchdog = WatchdogCounter(5, 2)
    while True:
        c = input("> ")
        print(watchdog.check(c, r".+"))


if __name__ == "__main__":
    test_watchdog()
