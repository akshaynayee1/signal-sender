# Data Publisher File
import paho.mqtt.client as paho
import json
import time
import datetime
import logging
from mqtt_credentials import broker_address,client_name, port, user, password, API_KEY,topic

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def on_publish(client, userdata, result):
    logger.info("Data Published to the Web Command Center")

def publish_data(client, status,health_status):
    current_time = datetime.datetime.now()
    data = {
        "fault_status": status,
        "timestamps": str(current_time),
        "device_api": API_KEY,
        "topic": topic,
        "device_status": "Active",
        "health_status": health_status
    }

    payload = json.dumps(data)
    ret = client.publish(topic, payload)
    logger.info(payload)

def setup_mqtt():
    client = paho.Client(client_name)
    client.username_pw_set(user, password=password)
    client.on_publish = on_publish
    client.connect(broker_address, port=port)
    return client

if __name__ == "__main__":
    mqtt_client = setup_mqtt()

    try:
        while True:
            publish_data(mqtt_client, "on","Fault ")
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Exiting program")
    finally:
        mqtt_client.disconnect()
