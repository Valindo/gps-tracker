import serial
import time
import paho.mqtt.client as mqtt
import json

# gps = serial.Serial('COM3',4800,timeout=0)
client = mqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)

def find_lat(temp):
    return temp.split(',')[3]

def find_long(temp):
    return temp.split(',')[5]
    

while(1):
    # temp = gps.readline()
    temp = "$GPRMC,113209.000,A,1529.0377,N,07348.8097,E,0.66,262.34,240318,,,A*69"
    if temp[0:6] == "$GPRMC":
        #Do the calculation for deg to decimal
        lat =  find_lat(temp)
        #Do the calculation for deg to decimal
        longi =  find_long(temp)
        data = { "lat": lat, "long": longi}
        client.publish('collegetest/raspberry', json.dumps(data), 0, False)
    time.sleep(.500)