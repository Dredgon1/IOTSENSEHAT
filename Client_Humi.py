import paho.mqtt.client as mqtt

broker_address = "192.168.0.95"
list_size=5
humi_list = []

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("humidity")

def on_message(client, userdata, msg):
    curret_humidity=float(msg.payload.decode())
    humi_list.append(curret_humidity)
    Sum=sum(humi_list)
    avarage=Sum/len(humi_list)
    avarage=round(avarage,2)
    print("The avarage of the last "+str(len(humi_list))," Samples is "+str(avarage)," %Humidity")
    f=open("Humidity_data.txt","a")
    f.write(str(curret_humidity)+"\n")
    
    if len(humi_list)>list_size-1:
        del humi_list[0]


client = mqtt.Client("192.168.0.13")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_forever()