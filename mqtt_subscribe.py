import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    """Prints formatted message from broker in standard character encoding"""
    # Converts data from binary to float
    data = float(message.payload.decode("utf-8"))
    print(f"Received message: {data}")

# Initialise connection to broker
topic = "TEMPERATURE"
port = 1883
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(mqttBroker, port)

# Subscribe to broker to  get data from a particular topic
client.subscribe(topic)

# Displays returned message as formatted in the function
client.on_message = on_message

# loop through infinitely to continously fetch data
client.loop_forever()