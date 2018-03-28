import serial
import time

# gps = serial.Serial('COM3',4800,timeout=0)

def find_lat(temp):
    return temp.split(',')[3]

def find_long(temp):
    return temp.split(',')[5]
    

while(1):
    # temp = gps.readline()
    temp = "$GPRMC,113209.000,A,1529.0377,N,07348.8097,E,0.66,262.34,240318,,,A*69"
    if temp[0:6] == "$GPRMC":
        print find_lat(temp)
        print find_long(temp)
        print '\n\n'
    time.sleep(.500)