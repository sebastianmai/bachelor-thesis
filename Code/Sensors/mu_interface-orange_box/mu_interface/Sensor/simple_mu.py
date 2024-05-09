import serial
import time

PORT = '/dev/ttyACM0'
BAUDRATE = 460800
INT = 1000

# Initialize serial port.
ser = serial.Serial(
    port=None,
    baudrate=BAUDRATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1,
    xonxoff=False,
    rtscts=True,
    dsrdtr=False
)

# Open the port.
ser.port = PORT
ser.rts = True
ser.dtr = False
time.sleep(0.1)
ser.open()
time.sleep(0.1)

ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(0.1)
print("Port opened.")

time.sleep(5.0)
print("Starting measurements...")

# Set measurement interval.
set_interval = ',mi{:05}*'.format(INT)
ser.write(set_interval.encode())

# Start measurements.
ser.write(b',ms*')

time.sleep(5.0)

# Read measurements.
while ser.in_waiting:
    print(ser.read(1).decode('ascii'), end='')
print()
time.sleep(1.0)

# Stop measurements.
print("Stopping measurements...")
ser.write(b',mp*')
time.sleep(0.1)
ser.write(b',sr*')
time.sleep(1.0)

# Close the port.
ser.close()
time.sleep(1)