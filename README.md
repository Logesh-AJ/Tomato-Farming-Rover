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
* 📡 Live video streaming using ESP32-CAM
* 🌡️ Environmental monitoring using sensors
* ⚡ Real-time inference using YOLOv8
* 🔁 Supports manual control and future autonomous extension

---

## 📡 ESP32-CAM Setup & Connectivity

The ESP32-CAM is configured in **Wi-Fi Access Point (Hotspot) mode** to enable direct communication with the processing system.

### 🔧 Configuration

* ESP32-CAM creates a hotspot
* Example:

  * SSID: `ESP32-CAM`
  * Password: `12345678`

### 📶 Connection Steps

1. Power ON the ESP32-CAM
2. Connect your laptop to the ESP32-CAM Wi-Fi network
3. Ensure the camera server is running
4. Access the video stream using:

```bash
http://192.168.4.1:81/stream
```

---

## ⚙️ System Workflow

1. **Image Capture**

   * ESP32-CAM captures real-time images

2. **Data Transmission**

   * Stream sent over Wi-Fi to processing system

3. **AI Processing**

   * YOLOv8 Model 1 → Tomato ripeness detection
   * YOLOv8 Model 2 → Disease detection

4. **Output**

   * Real-time bounding box predictions
   * Decision support for farming operations

---

## 🎥 Demo Video

[▶ Watch Rover System Demo](https://youtu.be/SywYewA_Va4?si=rCqZMHQAIErBjxgq)

---

## ⚡ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Logesh-AJ/Tomato-Farming-Rover.git
```

### 2. Navigate to project directory

```bash
cd Tomato-Farming-Rover
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Connect to ESP32-CAM

* Turn ON ESP32-CAM
* Connect to its Wi-Fi hotspot

### 5. Run live detection (ESP32 stream)

```bash
python src/main_stream.py
```

### 6. Run local webcam detection (optional)

```bash
python src/main_local.py
```

---

## ⚙️ System Requirements

* Python >= 3.8
* Webcam (for local testing)
* ESP32-CAM module (for live rover stream)
* Wi-Fi connectivity
* OS: Windows / Linux / macOS

---

## 📦 Dependencies

* ultralytics
* opencv-python
* numpy
* requests
* Pillow

---

## 📁 Project Structure

```bash
Tomato-Farming-Rover/
 ├── src/
 │    ├── camera/
 │    ├── training/
 │    ├── main_stream.py
 │    └── main_local.py
 ├── model/
 ├── demo_images/
 ├── research_paper/
 ├── Demo Videos
 ├── README.md
 └── requirements.txt
```

---

## 📄 Research Paper

This work is published in IEEE conference (ICEARS 2026).

👉 View details:
`research_paper/paper_link.md`

---

## 📌 Applications

* Precision agriculture
* Smart farming systems
* Crop health monitoring
* Automated irrigation decision support

---

## 🚧 Future Improvements

* Autonomous navigation system
* Edge deployment (Jetson Nano / Raspberry Pi)
* Robotic harvesting integration
* Full farm automation system

---

## 👤 Author

**Logesh A J**
AI | Computer Vision | Embedded Systems

---
