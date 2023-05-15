import paho.mqtt.client as mqtt

broker_address = "192.168.0.95"
list_size=5
temp_list = []

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("temperature")

def on_message(client, userdata, msg):
    curret_temperture=float(msg.payload.decode())
    temp_list.append(curret_temperture)
    Sum=sum(temp_list)
    avarage=Sum/len(temp_list)
    avarage=round(avarage,2)
    print("The avarage of the last "+str(len(temp_list))," Samples is "+str(avarage),"Degree celsius")
    f=open("Tempertune_data.txt","a")
    f.write(str(curret_temperture)+"\n")
    
    if len(temp_list)>list_size-1:
        del temp_list[0]


client = mqtt.Client("192.168.0.13")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_forever()