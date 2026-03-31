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
