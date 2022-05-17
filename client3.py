import paho.mqtt.client as mqtt
from multiprocessing import Process

brocker = "127.0.0.1"
sub_topic = "test/light"
pub_topic = "test/door"


def disconnect():
    client.disconnect()
    p.terminate()
    print("disconnect!")
    exit()

def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    if msg == "!":
        disconnect()
        return
    print(msg)

def publish(msg):
    client.publish(pub_topic, msg)

def Listen():
    client.loop_forever()

def run_Listen():
    client.on_message = on_message
    client.subscribe(sub_topic)
    p.start()



client = mqtt.Client()
client.connect(brocker, 1883, 60)

p = Process(target = Listen)
run_Listen()

print("ready to sub(light) and pub(door): ")
while True:
    msg = input()
    if msg == "~":
        break
    publish(msg)

print("publishing ended!")

disconnect()