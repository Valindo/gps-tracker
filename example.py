import time
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)

latValue = 15.4759923
longValue = 73.8126884
dataSet = []

for i in range(0,10):
    latValue = latValue + 1 * 10 ** -6
    longValue = longValue + 1 * 10 ** -6
    dataSet.append({
        "lat": latValue,
        "long": longValue
    })

for i in dataSet:
    client.publish('collegetest/raspberry', json.dumps(i), 0, False)
    time.sleep(1)