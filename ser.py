import serial
ser = serial.Serial('/dev/ttyUSB1', 9600)
while True:
    print ser.readline()
