import paho.mqtt.client as mqtt
import time

def retrieve_mqtt_message():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.subscribe("weather/#")
        else:
            print("Connection failed")

    def on_message(client, userdata, message):
        topic = message.topic
        payload = message.payload.decode("utf-8")

        print(f"Message received on topic {topic}: {payload}")

        if topic == "weather/temperature":
            client.temperature = payload
            client.disconnect()

    # MQTT client setup
    client = mqtt.Client("MQTT")
    client.username_pw_set("ramidi002", password="Karnan@25")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("172.20.122.185", 1883)
    client.loop_start()

    client.temperature = None
    while client.temperature is None:
        time.sleep(0.1)

    client.loop_stop()
    return client.temperature

if __name__ == "__main__":
    temperature = retrieve_mqtt_message()
    print(f"Retrieved Temperature: {temperature}")
