import paho.mqtt.client as mqtt

brocker = "127.0.0.1"
sub_topic = "test/light"

def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    if msg == "!":
        disconnect()
        return
    print(msg)

def disconnect():
    client.disconnect()


client = mqtt.Client()
client.connect(brocker, 1883, 60)

client.on_message = on_message
client.subscribe(sub_topic)
client.loop_forever()