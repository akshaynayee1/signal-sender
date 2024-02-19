import time
from gpiozero import Button
# Assuming mqtt_publisher and mqtt_credentials are available modules with the necessary functions
from mqtt_publisher import publish_data, setup_mqtt
from mqtt_credentials import API_KEY

# Setup the button on GPIO pin 19
button = Button(19)

def get_button_state():
    # Returns False when the button is pressed due to the pull-up resistor configuration
    return not button.is_pressed

if __name__ == "__main__":
    mqtt_client = setup_mqtt()
    status = ""
    health_status = ""

    try:
        while True:
            button_state = get_button_state()

            if button_state:
                print("Fault Signal Status - Flag OFF!")
                status = "OFF"
                health_status = "No Fault Occurs"
            else:
                print("Fault Signal Status - Flag ON!")
                status = "ON"
                health_status = "Fault Occurs"

            publish_data(mqtt_client, status, health_status)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        # Here you might want to clean up resources, for example, disconnect the MQTT client
        pass
