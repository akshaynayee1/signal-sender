# Signal Sender
One of the major components of the Virtual Fault Current Limiting (vFCL) System
Signal Sender is an **IoT edge-device communication module** that sends real-time electrical fault signals from field devices to a web dashboard using the **MQTT publish/subscribe mechanism**.

This project is part of a real-time electrical fault monitoring system. When an electrical fault occurs, the Raspberry Pi reads the device signal through GPIO, prepares a JSON payload, and publishes the fault event to an MQTT broker. The web dashboard can subscribe to the same MQTT topic and display the fault status, device health, timestamp, and waveform data in real time.

---

## What This Project Does

- Detects electrical fault status from a Raspberry Pi GPIO input.
- Publishes real-time fault status using MQTT.
- Sends structured JSON payloads to a broker/server.
- Supports device health monitoring such as `Fault Occurs` or `No Fault Occurs`.
- Sends waveform/sample signal data from CSV files in batches.
- Enables a web dashboard to visualize device status and fault events in real time.

---

## System Architecture

```text
┌───────────────────────┐
│   Electrical System   │
│   Power Line / VFCL   │
└───────────┬───────────┘
            │
            │ Fault Occurs
            ▼
┌───────────────────────┐
│ Fault Detection Unit  │
│ Sensors / Relay       │
└───────────┬───────────┘
            │ GPIO Signal
            ▼
┌───────────────────────┐
│ Raspberry Pi Edge     │
│ Signal Sender         │
│                       │
│ • Reads GPIO status   │
│ • Processes fault data│
│ • Creates JSON payload│
└───────────┬───────────┘
            │ MQTT Publish
            ▼
┌───────────────────────┐
│ MQTT Broker           │
│ Publish / Subscribe   │
└───────────┬───────────┘
            │ MQTT Subscribe
            ▼
┌───────────────────────┐
│ Web Dashboard         │
│                       │
│ • Fault status        │
│ • Device health       │
│ • Waveform data       │
│ • Real-time alerts    │
└───────────────────────┘
```

---

## MQTT Data Flow

1. Electrical fault occurs in the monitored device/system.
2. Fault signal is detected through the Raspberry Pi GPIO pin.
3. Signal Sender reads the GPIO status.
4. The application creates a JSON payload with fault status and device information.
5. Payload is published to the configured MQTT topic.
6. MQTT broker forwards the message to subscribed applications.
7. Web dashboard receives and displays the real-time fault event.

---

## Example MQTT Payload

```json
{
  "fault_status": "ON",
  "timestamps": "2024-02-21 15:21:00",
  "device_api": "DEVICE_API_KEY",
  "topic": "mqttdevice/",
  "device_status": "Active",
  "health_status": "Fault Occurs"
}
```

When no fault is present, the payload changes to:

```json
{
  "fault_status": "OFF",
  "device_status": "Active",
  "health_status": "No Fault Occurs"
}
```

---

## Project Files

| File | Description |
|---|---|
| `button_program.py` | Reads the Raspberry Pi GPIO button/signal and publishes fault ON/OFF status. |
| `mqtt_publisher.py` | Handles MQTT client setup and publishes JSON payloads. |
| `signals_publisher_v_0.1.py` | Sends waveform/sample signal data in batches through MQTT. |
| `mqttSubscribeClass.py` | MQTT subscriber helper class. |
| `mqtt_credentials.py` | Stores MQTT broker configuration, topic, username, password, and API key. |
| `sample_data.csv` | Sample waveform/signal data used for batch transmission. |
| `waveSignals.csv` | Wave signal dataset. |
| `file_generator.py` | Utility script for generating files/data. |
| `Jsongenerate.py` | Utility script for generating JSON data. |

---

## Technologies Used

- Python
- Raspberry Pi GPIO
- MQTT
- Eclipse Paho MQTT Client
- Pandas
- JSON
- CSV waveform data
- IoT edge-device communication

---

## Hardware / Device Layer

The project uses a Raspberry Pi as an edge device. GPIO pin `19` is used to read the fault signal.

```python
button = Button(19)
```

The button/signal state represents whether the electrical fault flag is active or inactive.

---

## How It Works

### Fault ON

When the fault signal is active:

```text
fault_status = ON
health_status = Fault Occurs
```

The data is sent to the MQTT broker and then displayed on the web dashboard.

### Fault OFF

When the fault signal is inactive:

```text
fault_status = OFF
health_status = No Fault Occurs
```

The dashboard receives the updated status in real time.

---

## Setup

### 1. Install Dependencies

```bash
pip install paho-mqtt gpiozero pandas
```

### 2. Configure MQTT Credentials

Update `mqtt_credentials.py` with your broker details:

```python
broker_address = "YOUR_BROKER_IP"
port = 1883
user = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
topic = "YOUR_TOPIC"
API_KEY = "YOUR_DEVICE_API_KEY"
```

### 3. Run the Signal Sender

```bash
python button_program.py
```

To publish waveform batches:

```bash
python signals_publisher_v_0.1.py
```

---

## Use Case

This project is useful for:

- Electrical fault monitoring
- VFCL fault signal transmission
- Industrial IoT monitoring
- Real-time device health dashboards
- Remote fault detection systems
- MQTT-based telemetry pipelines

---

## Resume Description

**Short version:**

> Built an MQTT-based IoT signal sender that streams real-time electrical fault events from Raspberry Pi edge devices to a web dashboard for fault visualization and device health monitoring.

**Detailed version:**

> Designed and implemented a Raspberry Pi-based IoT signal sender for real-time electrical fault monitoring using MQTT. The system reads fault signals through GPIO, converts device status into JSON payloads, publishes telemetry to an MQTT broker, and enables a web dashboard to display fault status, waveform data, timestamps, and device health in real time.

---

## Security Note

Do not commit real MQTT credentials, API keys, usernames, or passwords to GitHub. Use an `.env` file or environment variables instead.

Example:

```bash
MQTT_BROKER=your_broker_ip
MQTT_USER=your_username
MQTT_PASSWORD=your_password
MQTT_TOPIC=mqttdevice/
DEVICE_API_KEY=your_api_key
```

---

