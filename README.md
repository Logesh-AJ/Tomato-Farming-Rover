# 🚜 Intelligent YOLOv8-Based Rover for Precision Agriculture

AI-powered rover system for real-time tomato ripeness classification and disease detection using computer vision and IoT-based environmental monitoring.

---

## 🧠 Tech Stack

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* ESP32-CAM
* IoT Sensors (Soil Moisture, Humidity, Water Level)

---

## 🚀 Key Features

* 🍅 Tomato ripeness detection (Ripe / Unripe classification)
* 🌿 Multi-class plant disease detection
* 📡 Live image streaming using ESP32-CAM
* 🌡️ Environmental monitoring (soil moisture, humidity)
* ⚡ Real-time inference using YOLOv8 models
* 🔁 Bidirectional communication for control and monitoring

---

## 🏗️ System Architecture

The system consists of a rover equipped with sensors and an ESP32-CAM module that captures images and streams them over Wi-Fi to a processing unit.

* Image data → processed using YOLOv8 models
* Sensor data → used for irrigation insights
* Results → sent back for monitoring and control

---

## ⚙️ Workflow

1. **Data Acquisition**

   * Images captured using ESP32-CAM
   * Environmental data collected from sensors

2. **Data Transmission**

   * Live streaming via Wi-Fi to processing system

3. **AI Processing**

   * YOLOv8 Model 1 → Tomato ripeness detection
   * YOLOv8 Model 2 → Disease detection

4. **Output & Decision Making**

   * Results displayed in real-time
   * Enables data-driven farming decisions

---

## 📡 ESP32-CAM Setup & Connectivity

The ESP32-CAM module is configured to operate in Wi-Fi Access Point (Hotspot) mode to enable direct communication with the processing system.

### 🔧 Configuration

* The ESP32-CAM creates a Wi-Fi hotspot (SSID configured in the firmware)
* Example:

  * SSID: `ESP32-CAM`
  * Password: `12345678`

### 📶 Connection Process

1. Power on the ESP32-CAM module
2. Connect the laptop to the ESP32-CAM Wi-Fi hotspot
3. The ESP32-CAM starts a local server (HTTP stream)
4. The video stream is accessed using the IP address and port

### 🌐 Stream Access

The camera stream is accessed in Python using:

```python
http://192.168.4.1:81/stream
```

* `192.168.4.1` → Default IP of ESP32-CAM in AP mode
* `81` → Port used for video streaming

### 🧠 Integration with Python

* OpenCV is used to capture frames from the stream
* Frames are processed using YOLOv8 models for:

  * Tomato ripeness detection
  * Disease classification

### ⚠️ Important Notes

* The ESP32-CAM hotspot must be ON before running the Python script
* The system will not connect if:

  * Wi-Fi is not connected to ESP32-CAM
  * Incorrect IP/port is used
  * Camera server is not running

---


## 📊 Model Performance

### 🍅 Ripeness Detection

* Precision: ~95% (Ripe), ~93% (Unripe)

### 🌿 Disease Detection

* Precision: >94% for most disease classes

*(Based on experimental evaluation results)*

---

## 📸 Results

![Detection Output](demo_images/sample1.png)

---

## 🎥 Demo

[▶ Watch Full Demo](https://youtube.com/your-link)

---

## ⚡ How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/yolov8-agri-rover-tomato-detection.git
```

2. Navigate to project directory

```bash
cd yolov8-agri-rover-tomato-detection
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run detection

```bash
python src/main.py
```

---

## ⚙️ System Requirements

* Python >= 3.8
* Webcam / ESP32-CAM
* Wi-Fi connectivity
* OS: Windows / Linux / macOS

---

## 📦 Dependencies

* ultralytics
* opencv-python
* numpy

---

## 📁 Project Structure

```bash
yolov8-agri-rover-tomato-detection/
 ├── src/
 │    ├── main.py
 │    ├── detect.py
 │    └── utils.py
 ├── models/
 │    ├── ripeness_model.pt
 │    └── disease_model.pt
 ├── demo_images/
 ├── demo_video/
 ├── README.md
 └── requirements.txt
```

---

## 🚧 Future Improvements

* Onboard deployment using NVIDIA Jetson Nano
* Autonomous navigation system
* Robotic arm for automated harvesting
* Precision irrigation and pesticide control
* Fully autonomous farming system

---

## 📌 Applications

* Smart agriculture
* Precision farming
* Crop health monitoring
* Automated irrigation systems

---

## 👤 Author

**Logesh A J**
Electronics & Communication Engineering | AI & Embedded Systems

---
