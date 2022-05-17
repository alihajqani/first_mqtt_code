import paho.mqtt.client as mqtt

# settings
brocker = "127.0.0.1"
pub_topic = "test/light"

def publish(msg):
    client.publish(pub_topic, msg)
    
client = mqtt.Client()
client.connect(brocker, 1883, 60)


while True:
    msg = input("ready to pub(light): ")
    if msg == "~":
        break
    publish(msg)

print("publishing ended!")

client.disconnect()