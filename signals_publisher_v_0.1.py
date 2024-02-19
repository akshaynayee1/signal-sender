import time
from gpiozero import Button
import paho.mqtt.client as paho
import json
import datetime
import pandas as pd
from mqtt_credentials import broker_address, client_name, port, user, password, API_KEY, topic

# Setup the button on GPIO pin 19
button = Button(19)

# MQTT Client Setup
client = paho.Client(client_name, protocol=paho.MQTTv5)
client.username_pw_set(user, password=password)

def on_publish(client, userdata, mid):
    print("Data batch published.")

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code "+str(rc))

client.on_connect = on_connect
client.on_publish = on_publish
client.connect_async(broker_address, port=port)
client.loop_start()

def publish_data(client, status, health_status):
    batch_data = read_and_batch_data('waveSignals.csv')
    for batch in batch_data:
        payload = json.dumps({
            "fault_status": status,
            "device_api": API_KEY,
            "topic": topic,
            "device_status": "Active",
            "health_status": health_status,
            "timestamp": datetime.datetime.now().isoformat(),
            "data": batch,
        })
        client.publish(topic, payload, qos=0)
        time.sleep(1)  # Throttle batch sending

def read_and_batch_data(file_path, batch_size=100):
    df = pd.read_csv(file_path)
    batches = [df[i:i+batch_size].to_dict(orient='records') for i in range(0, df.shape[0], batch_size)]
    return batches

def on_button_press():
    print("Button was pressed. Sending data with status ON.")
    publish_data(client, "ON", "Fault Occurs")

def on_button_release():
    print("Button was released. Sending data with status OFF.")
    publish_data(client, "OFF", "No Fault Occurs")

button.when_pressed = on_button_press
button.when_released = on_button_release

try:
    print("Ready. Waiting for button press/release to send data.")
    while True:
        time.sleep(0.1)  # Small delay to keep the loop from consuming too much CPU
except KeyboardInterrupt:
    print("Exiting program")
finally:
    client.loop_stop()
    client.disconnect()

