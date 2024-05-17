#!/usr/bin/env python3
import os
import csv
import yaml
from datetime import datetime
from pathlib import Path

from mu_interface.Utilities.utils import TimeFormat


class data2csv:
    transformations = {
        "temp_external": (lambda d, c: d[c] / 10000),                                     # Degrees Celsius
        "temp_PCB": (lambda d, c: d[c] / 10000),                                          # Degrees Celsius
        "soil_temperature": (lambda d, c: d[c] / 10),                                     # Degrees Celsius
        "mag_X": (lambda d, c: d[c] / 1000 * 100),                                        # Micro Tesla
        "mag_Y": (lambda d, c: d[c] / 1000 * 100),                                        # Micro Tesla
        "mag_Z": (lambda d, c: d[c] / 1000 * 100),                                        # Micro Tesla
        "light_external": (lambda d, c: d[c] / 799.4 - 0.75056),                          # Lux
        "humidity_external": (lambda d, c: (d[c] * 3 / 4200000 - 0.1515) \
                                / (0.006707256 - 0.0000137376 * d["temp_external"])),     # Percent
        "air_pressure": (lambda d, c: d[c] / 100),                                        # Mili Bars
        "differential_potential_CH1": (lambda d, c: (d[c] - 512000) / 1000),              # Mili Volts
        "differential_potential_CH2": (lambda d, c: (d[c] - 512000) / 1000),              # Mili Volts
        "transpiration": (lambda d, c: d[c] / 1000),                                      # Percent
        "RMS_CH1": (lambda d, c: d[c] * 0.000000095427163),
        "RMS_CH2": (lambda d, c: d[c] * 0.000000095427163),
        "sweep_freq": (lambda d, c: d[c] / 10)                                           # Hz
    }

    rounding = {
        "temp_external": 2,
        "temp_PCB": 2,
        "soil_temperature": 2,
        "mag_X": 2,
        "mag_Y": 2,
        "mag_Z": 2,
        "light_external": 1,
        "humidity_external": 2,
        "air_pressure": 2,
        "differential_potential_CH1": 3,
        "differential_potential_CH2": 3,
        "transpiration": 2,
    }

    def __init__(self, file_path, file_name, additionalSensors, config_file=None):
        self.file_path = Path(file_path)
        self.file_path.mkdir(parents=True, exist_ok=True)  # make new directory
        self.file_name = file_name
        self.additionalSensors = additionalSensors

        if additionalSensors == "energy":
            # TODO: separate from mu_interface
            self.header = [
                "bus_voltage_solar",
                "current_solar",
                "bus_voltage_battery",
                "current_battery",
                "temperature",
                "humidity",
            ]
        else:
            if config_file is None:
                config_file = Path(__file__).parent.absolute() / "config/custom_data_fields.yaml"
                if not config_file.exists():
                    config_file = Path(__file__).parent.absolute() / "config/default_data_fields.yaml"

            with open(config_file) as stream:
                config = yaml.safe_load(stream)

            # Names of stored columns.
            self.header = [key for key in config if config[key]] + additionalSensors
            # Indices of stored columns.
            self.filter = [i for i, x in enumerate(config.values()) if x] + list(
                range(len(config), len(config) + len(additionalSensors))
            )

        with open(self.file_path / self.file_name, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["datetime"] + self.header)

    def fix_ownership(self):
        """Change the owner of the file to SUDO_UID"""
        uid = os.environ.get("SUDO_UID")
        gid = os.environ.get("SUDO_GID")
        if uid is not None and gid is not None:
            full_path = self.file_path / self.file_name
            os.chown(full_path, int(uid), int(gid))
            for p in list(full_path.parents)[:-3]:
                os.chown(p, int(uid), int(gid))

    def write2csv(self, data):
        try:
            if self.additionalSensors == "energy":
                timestamp = datetime.fromtimestamp(data[0])
                filtered_data = data[1:]
            else:
                timestamp = datetime.fromtimestamp(data[3]).strftime(TimeFormat.data)
                filtered_data = [data[i] for i in self.filter]
                # df = DataFrame(data=[filtered_data], columns=self.header)
                # filtered_data = data2csv.transform_data(df)
                filtered_data = data2csv.transform_data(filtered_data, self.header)

            data4csv = [timestamp] + filtered_data
            with open(self.file_path / self.file_name, "a", newline="") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(data4csv)

        except Exception as e:
            return e

    # @staticmethod
    # def transform_data(df):
    #     for column in df.columnsns:
    #         if column in data2csv.transformations:
    #             df[column] = round(data2csv.transformations[column](df, column), data2csv.rounding[column])

    #     return df.iloc[0].tolist()

    @staticmethod
    def transform_data(data, header):
        df = {header[i]: data[i] for i in range(len(data))}
        for i in range(len(data)):
            key = header[i]
            if key in data2csv.transformations:
                data[i] = round(data2csv.transformations[key](df, key), data2csv.rounding.get(key, 2))

        return data
