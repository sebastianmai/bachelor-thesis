#!/bin/bash

scripts=(
    "/home/pi/DATA/CODE/Sensors/mu_interface-orange_box/mu_interface/Sensor/main.py"
    "/home/pi/DATA/CODE/Sensors/Phyto/thread.py"
    "/home/pi/DATA/CODE/Sensors/Temp/serialTemperatur.py"
    "/home/pi/DATA/CODE/Experiments/experiments_control_heat.py"
)

for script in "${scripts[@]}"; do
    lxterminal -e "bash -c 'python3 $script; exec bash'" &
done