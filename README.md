# IOTSENSEHAT
code for group PR-4 for IOT (2023)

please note this project uses paho mqtt(MOM) and mosquitto(broker)
also remember the broker and client IPs needs to be changed
the MOM and broker run on the same computer in our case and as such we use its IPv4 IP for both cases
the client (raspi) and other laptops(clients that want data) need the broker/MOM IP to work AND need to be placed on the same network.

mosquitto link: https://mosquitto.org/download/
paho link: https://pypi.org/project/paho-mqtt/

we ran mosquitto on a windows laptop, it requires some setup and you have to run it with CMD with the mosquitto.conf
in the conf file you need to do:

allow_anonymous enabled
listener 1883 

you can search for both of them and in the mosquitto.conf file and uncomment them
then in windows you need to edit enviromental variables in order to run mosquitto
remember to run mosquitto in CMD like this: mosquitto -c C:\mosquitto\mosquitto.conf -v
with "C:\mosquitto\" replaced with whever you placed the mosquitto directory.
