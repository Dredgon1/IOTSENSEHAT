import paho.mqtt.client as mqtt
import json

client_address = "192.168.43.146"
broker_address = "192.168.43.146"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor_data")

def on_message(client, userdata, message):
    payload_dict = json.loads(message.payload.decode('utf-8'))
    
    # Extract data from json
    temperature = payload_dict['temperature']
    humidity = payload_dict['humidity']
    pressure = payload_dict['pressure']

    #publish data to clients
    client.publish("temperature", "{:.2f}".format(temperature))
    client.publish("humidity", "{:.2f}".format(humidity))
    client.publish("pressure", "{:.2f}".format(pressure))
    
    # Print sensor data
    print("Temperature: {:.2f} C".format(temperature))
    print("Humidity: {:.2f} %".format(humidity))
    print("Pressure: {:.2f} hPa".format(pressure))

# initialise client and all that other stuff
client = mqtt.Client(client_address)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_forever()
