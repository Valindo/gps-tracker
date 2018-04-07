import serial

import time

import paho.mqtt.client as mqtt

import json



gps = serial.Serial('/dev/ttyUSB0',4800,timeout=0)

client = mqtt.Client()

client.connect("iot.eclipse.org", 1883, 60)



def find_lat(temp):
    if temp.split(',')[3] !=  '':
    	x = float(temp.split(',')[3])
    	return round(int(x/100) + ((x%100)/60),6)
    return ''



def find_long(temp):
    if temp.split(',')[5] != '':
    	x = float(temp.split(',')[5])
    	return round(int(x/100) + ((x%100)/60),6)
    return ''

    



while(1):

   temp = gps.readline()

   # temp = "$GPRMC,042209.000,A,1519.6063,N,07356.0078,E,0.12,1.42,060418,,,A*6B"


   if temp[0:6] == "$GPRMC":

        #Do the calculation for deg to decimal

        lat =  find_lat(temp)

        #Do the calculation for deg to decimal

        longi =  find_long(temp)

        data = { "lat": lat, "long": longi}

        client.publish('collegetest/raspberry', json.dumps(data), 0, False)

   time.sleep(.500)
