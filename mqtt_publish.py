import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# Initialise connection to broker
topic = "TEMPERATURE"
port = 1883
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(mqttBroker, port)

# Publish random number to broker
while True:
    # Generate random number
    randNumber = uniform(30.0, 34.0)
    
    # Publish number to broker
    client.publish(topic, randNumber)
    
    # Display a confirmatory message
    print(f"Just published {str(randNumber)} to Topic TEMPERATURE")
    
    # Set a 1 sec interval
    time.sleep(1)