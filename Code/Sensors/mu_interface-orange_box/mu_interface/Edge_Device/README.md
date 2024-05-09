# Edge Device 
This directory contains the files only needed for the Edge Device, which will collect the data from the sensor nodes. The Edge Device also requires the directory *Utilities*.

### main.py
The entry point and only file that has to be executed to run the scripts.
### edge_device.py
Contains the main class *Edge_Device*, which handles the program logic of the edge device. It reads the data from the *zmq_subscriber* and writes it to .csv files
### zmq_subscriber.py
Contains the class *ZMQ_Subscriber* for wireless communication between sensor and edge device using [ZeroMQ](https://zeromq.org). It provides methods for sending numpy arrays and the multipart data message.
