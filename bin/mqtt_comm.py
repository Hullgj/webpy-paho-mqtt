import paho.mqtt.client as mqtt
from app import app

resp = "Nothing yet"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc) +
        "client_id " + str(client))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("unikent/co838/gjh9_example")
    # publish to a topic and send a message as a string
    # client.publish("unikent/co838/gjh9_example", "Hello World")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    data = {'mbed_data': str(msg.payload)}
    global resp 
    resp = app.request('/welcome', method="POST", data=data)
    # print resp
    # raw_input()
    # data = json.loads(web.data())
    # print data
    # raw_input()
    # mbed_data = data["myName"]
    # print mbed_data
    # raw_input()

def get_data():
    client = mqtt.Client("CO838 publisher (gjh9)", True)
    client.on_connect = on_connect
    client.on_message = on_message

    # client.connect("iot.eclipse.org", 1883, 60)
    # use client.connect_async for non-blocking connection
    # client.connect("mqtt.kent.ac.uk", 1883, 60)
    client.connect("broker.hivemq.com", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a manual interface.
    client.loop_start()
    return client

get_data()