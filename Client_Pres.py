import paho.mqtt.client as mqtt

broker_address = "192.168.0.95"
list_size=5
pres_list = []

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("pressure")

def on_message(client, userdata, msg):
    curret_pressure=float(msg.payload.decode())
    pres_list.append(curret_pressure)
    Sum=sum(pres_list)
    avarage=Sum/len(pres_list)
    avarage=round(avarage,2)
    print("The avarage of the last "+str(len(pres_list))," Samples is "+str(avarage),"mPa")
    f=open("Pressure_data.txt","a")
    f.write(str(curret_pressure)+"\n")
    
    if len(pres_list)>list_size-1:
        del pres_list[0]


client = mqtt.Client("192.168.0.13")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_forever()