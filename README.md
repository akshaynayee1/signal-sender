# ⚡ Signal Sender

### One of the Core Components of the Virtual Fault Current Limiting (VFCL) System

Signal Sender is an Industrial IoT edge communication module developed for the **Virtual Fault Current Limiting (VFCL) System**. The module enables real-time transmission of electrical fault events, device telemetry, and waveform data from field devices to a centralized monitoring platform using the MQTT publish-subscribe architecture.

By connecting the operational technology (OT) layer with cloud-connected monitoring applications, Signal Sender provides continuous visibility into electrical network conditions, enabling rapid fault detection, diagnostics, and response.

---

## 🚀 Overview

The Signal Sender module operates on a Raspberry Pi and receives fault indications from an ESP32-based fault detection unit. When an abnormal electrical condition is detected, the Raspberry Pi processes the fault signal, generates structured telemetry data, and publishes the event to an MQTT broker.

Subscribed applications, including web dashboards and monitoring services, receive fault notifications in real time and display system status, health metrics, timestamps, and waveform information.

---

## ✨ Key Features

* ⚡ Real-time electrical fault monitoring
* 📡 MQTT-based publish-subscribe communication
* 🖥️ Raspberry Pi edge-device integration
* 🔌 ESP32-based fault detection interface
* 📊 Waveform and telemetry transmission
* 📈 Device health monitoring
* 🚨 Instant fault notifications
* ☁️ Edge-to-cloud communication architecture
* 🔄 Low-latency event propagation
* 🏭 Industrial IoT monitoring support

---

# 🏗️ System Architecture

```text
┌─────────────────────────────┐
│    Electrical System        │
│  Power Line / VFCL Network  │
└─────────────┬───────────────┘
              │
              │ Fault Occurs
              ▼
┌─────────────────────────────┐
│ Fault Detection Unit        │
│ ESP32 Microcontroller       │
│                             │
│ • Voltage Monitoring        │
│ • Current Monitoring        │
│ • Fault Detection Logic     │
│ • Signal Acquisition        │
└─────────────┬───────────────┘
              │ GPIO Signal
              ▼
┌─────────────────────────────┐
│ Raspberry Pi Edge Device    │
│ Signal Sender Module        │
│                             │
│ • Reads Fault Status        │
│ • Processes Telemetry Data  │
│ • Creates JSON Payload      │
│ • Publishes MQTT Messages   │
└─────────────┬───────────────┘
              │ MQTT Publish
              ▼
┌─────────────────────────────┐
│ MQTT Broker                 │
│ Publish / Subscribe Layer   │
└─────────────┬───────────────┘
              │ MQTT Subscribe
              ▼
┌─────────────────────────────┐
│ Web Dashboard               │
│                             │
│ • Fault Status Monitoring   │
│ • Device Health Monitoring  │
│ • Waveform Visualization    │
│ • Real-Time Alerts          │
│ • Historical Event Tracking │
└─────────────────────────────┘
```

---

# ⚡ Fault Detection Unit – ESP32 Microcontroller

The ESP32 Microcontroller serves as the fault sensing and data acquisition layer of the VFCL platform.

The controller continuously monitors electrical parameters such as voltage, current, and protection signals from the VFCL system. When abnormal operating conditions such as overcurrent, short circuits, or transient disturbances are detected, the ESP32 immediately generates a fault indication signal.

The signal is transmitted to the Raspberry Pi through GPIO communication, allowing the Signal Sender module to publish real-time fault information to the MQTT infrastructure.

### Responsibilities

* ⚡ Voltage monitoring
* ⚡ Current monitoring
* 📊 Electrical signal acquisition
* 🚨 Fault detection and event triggering
* 🔌 GPIO communication
* 📡 Edge telemetry generation
* ⏱️ Low-latency fault reporting

---

# 🔄 MQTT Data Flow

1. ⚡ Electrical fault occurs in the VFCL system.
2. 📊 ESP32 detects abnormal electrical behavior.
3. 🚨 Fault trigger signal is generated.
4. 🔌 Raspberry Pi receives fault status through GPIO.
5. 📦 Signal Sender creates a JSON telemetry payload.
6. 📡 Payload is published to the MQTT broker.
7. ☁️ MQTT broker distributes the message to subscribers.
8. 🖥️ Web Dashboard displays fault status and system health in real time.

---

# 📄 Example MQTT Payload

```json
{
  "fault_status": "ON",
  "timestamp": "2024-02-21 15:21:00",
  "device_status": "Active",
  "health_status": "Fault Occurs",
  "topic": "mqttdevice/"
}
```

### No Fault Condition

```json
{
  "fault_status": "OFF",
  "device_status": "Active",
  "health_status": "No Fault Occurs"
}
```

---

# 📂 Project Structure

| File                         | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| `button_program.py`          | Reads GPIO fault signals and publishes fault status |
| `mqtt_publisher.py`          | MQTT client initialization and message publishing   |
| `signals_publisher_v_0.1.py` | Publishes waveform and signal datasets              |
| `mqttSubscribeClass.py`      | MQTT subscriber utility                             |
| `mqtt_credentials.py`        | MQTT configuration and broker settings              |
| `sample_data.csv`            | Sample signal data                                  |
| `waveSignals.csv`            | Waveform dataset                                    |
| `file_generator.py`          | Data generation utility                             |
| `Jsongenerate.py`            | JSON payload generation utility                     |

---

# 🛠️ Technology Stack

### Software

* Python
* MQTT
* Eclipse Paho MQTT
* Pandas
* JSON
* CSV Processing

### Hardware

* Raspberry Pi
* ESP32 Microcontroller
* Electrical Fault Detection Circuit

### Architecture

* Industrial IoT
* Edge Computing
* Publish-Subscribe Communication
* Real-Time Monitoring Systems

---

# 🔧 Installation

### Install Dependencies

```bash
pip install paho-mqtt gpiozero pandas
```

### Configure MQTT Broker

Update `mqtt_credentials.py`

```python
broker_address = "YOUR_BROKER_IP"
port = 1883
user = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
topic = "YOUR_TOPIC"
API_KEY = "YOUR_DEVICE_API_KEY"
```

---

# ▶️ Running the Application

### Start Fault Monitoring

```bash
python button_program.py
```

### Publish Waveform Data

```bash
python signals_publisher_v_0.1.py
```

---

# 🎯 Applications

* Smart Grid Monitoring
* Virtual Fault Current Limiting (VFCL) Systems
* Industrial Automation
* Power Distribution Networks
* Remote Asset Monitoring
* Predictive Maintenance Platforms
* Electrical Protection Systems
* Real-Time Fault Management

---

# 🔒 Security Best Practices

Never commit credentials, API keys, usernames, or passwords to source control.

Use environment variables instead:

```bash
MQTT_BROKER=your_broker_ip
MQTT_USER=your_username
MQTT_PASSWORD=your_password
MQTT_TOPIC=mqttdevice/
DEVICE_API_KEY=your_api_key
```

---

# 🚀 Future Enhancements

* AI-based fault prediction
* Waveform anomaly detection
* Cloud-based historical analytics
* Predictive maintenance dashboards
* Multi-device fleet monitoring
* AWS IoT Core integration
* Real-time alerting via Email/SMS
* Machine Learning-powered fault classification

---

# 📖 Project Summary

Designed and developed an MQTT-based edge communication module for a Virtual Fault Current Limiting (VFCL) System. Implemented Raspberry Pi GPIO-based fault acquisition, real-time telemetry processing, and MQTT message publishing to enable low-latency transmission of electrical fault events, device health metrics, and waveform data to centralized monitoring dashboards.

By AkshayKumar Nayee -  Graduate Research Assistant | Gannon University & Dr.Fong Mak
