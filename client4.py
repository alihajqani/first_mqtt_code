import paho.mqtt.client as mqtt

brocker = "127.0.0.1"
sub_topics = [("test/light", 0), ("test/door", 1)]

def disconnect():
    client.disconnect()
    print("disconnect!")
    exit()

def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    if msg == "!":
        disconnect()
        return
    print("received: ", msg)

client = mqtt.Client()
client.connect(brocker, 1883, 60)



client.on_message = on_message

client.subscribe(sub_topics)

client.loop_forever()