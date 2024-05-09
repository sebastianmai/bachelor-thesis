#!/usr/bin/env python3
import os
import sys
import logging
import argparse
from pathlib import Path

from edge_device import Edge_Device
from mu_interface.Utilities.log_formatter import setup_logger

def main(csv_dir, fields_cfg):
    setup_logger("rock")
    logging.info("Starting edge node.")

    csv_dir = Path(csv_dir)
    
    # If args.cfg is None, look for a file in the current directory
    fields_cfg = None
    if args.cfg is None:
        custom_cfg = Path(sys.executable).parent.absolute() / 'custom_data_fields.yaml'
        print(custom_cfg)
        if custom_cfg.exists():
            fields_cfg = custom_cfg
    else:
        fields_cfg = Path(args.cfg)
            

    ED = Edge_Device(csv_dir, fields_cfg)
    while True:
        try:
            ED.start()
        except KeyboardInterrupt:
            ED.stop()
            
            next_command = input('\nEnter a command:\n\tnew --> start new measurement\n\texit --> exit from the script\n> ')
            if next_command != 'new':
                if next_command != 'exit':
                    print("Unknow command. Exiting.")
                ED.shutdown()
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments for the sensor node.")
    parser.add_argument('--dir', action='store', default=Path.home() / 'measurements')
    parser.add_argument('--cfg', action='store', default=None)
    args = parser.parse_args()
        
    main(args.dir, args.cfg)
    