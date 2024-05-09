# WatchPlant data collection setup

This is the planned structure for the WatchPlant data collection setup. The scripts in the folder Edge_Device will run on one RPi to collect data, the scripts in the folder Sensor will run on RPis connected to a Cybres MU. *Utilities* are required by all RPis. On both the Edge Device and Sensor is one *main.py* file. They are the starting point and the only files that must be executed.

## Needed software
To run the scripts, a python 3 installation is needed. It is recommended to use a virtual environment (for example `venv`). You need to install the following packages: 
```bash
pip3 install pyserial numpy zmq pyyaml
```
Note: Both the packages *zmq* and *pyzmq* work.

To use the real-time plottinf with *app.py*, the following additional packages are needed:
```bash
pip3 install pandas dash dash-bootstrap-components
```

**IMPORTANT**: In order for imports to work properly, this package needs to be installed. Navigate to the root of the repository (.../**mu_interface**/mu_interface/...) and run:
```bash
pip3 install -e .
```

## Default Data Fields
The file *data_fields.yaml* in the *Utilities* folder contains the default configuration for data fields from the MU. It can be changed to include more or less MU data fields.

## Additional Sensors
The setup can be used with a variable number of additional sensors. To include them, only the code of the Sensor Node has to be changed, the Edge Device adapts itself to the additional sensors. Additional values will also be saved in the .csv file, exactly as the default values from the MU. To add a sensor, change two lines in the file *sensor_node.py*:

- Line 33: Add the names of the additional data columns (header in the csv file) to the list self.additionalSensors. If only the MU is used, this list has to be empty.
- Line 135: Add the data values to the list additionalValues. It is advised to write a new class for new sensors, similar to *cybres_mu.py*, and implement some kind of getData() method.

The number of elements in both lists has to be the same, so one value correlates to exactly one data column header and vice versa.

## File saving
The measured data gets saved as .csv file both on the Sensor Node and the Edge Device. Default location for the Sensor Node resp. Edge Device are ``/home/$USER/measurements`` resp. ``/home/$USER/measurements/hostname``, where ``hostname`` is the hostname of the Sensor Node which sent the data.

The hostnames should be named as ``rpi[index]``, e.g.: ``rpi0``, ``rpi1``, ...

## Sending data
Edge Device and Sensor Nodes communicate wirelessly using [ZeroMQ](https://zeromq.org/). Depending on the local network setup, the addresses in the classes *ZMQ_Publisher* and *ZMQ_Subscriber* must be changed. Refer to [the ZMQ documentation](http://api.zeromq.org/3-2:zmq-tcp) for more information.

## Message format
ZMQ allows to send custom message formats using [multipart messages](http://api.zeromq.org/3-2:zmq-send). Every message send to the edge device consists of two parts: The header and the payload. The header is a python dictionary with three entries, the first is the Sensor Node's hostname. The second is an integer between 0 and 2 and specifies the type of payload (the MU can send three different message types):
|Number|Message Type|Payload|
|---|---|---|  
| 0 | MU data header | String|
| 1 | Measurement Data | numpy array|
| 2 | Measurement Data/ID/Mode | numpy array|

The third header entry is a boolean flag that indicates if additional sensors other than the MU are used. If the flag is True, an additional message part between header and payload is sent which contains the names of the additional data columns for saving in the .csv file.

The measurement data array consists of a timestamp generated on the Sensor Node RPi, followed by sensor metadata (MU ID, MU MM, sensor hostname) and the measured data. If additional sensors are used, the additional values are attached to the measured data array.

## Real-Time plot
Running *app.py* starts an interactive dashboard on a local port (default: http://127.0.0.1:8050/). Open this port in a any browser to observe the running experiment.

