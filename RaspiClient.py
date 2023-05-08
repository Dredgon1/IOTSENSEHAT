import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

broker_address = "192.168.43.146" # use mom and broker address!!!

client = mqtt.Client()
client.connect(broker_address)
sense=SenseHat()

while True:
	temp=sense.get_temperature()
	hum=sense.get_humidity()
	pres=sense.get_pressure()
	
	
	payload = json.dumps({'temperature':temp,'humidity':hum,'pressure':pres})

	client.publish("sensor_data", payload)
	time.sleep(5)

