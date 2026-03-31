import cv2
import requests
import numpy as np
import time
import tkinter as tk
from PIL import Image, ImageTk
from ultralytics import YOLO
import threading

# ---------------- CONFIG ----------------
CAM_URL = "http://192.168.137.200/capture"

# Load YOLO models
MODEL1 = YOLO(r"C:\Users\logesh A.J\Documents\projects\farming_rover\main\ripe_unripe_best.pt")
MODEL2 = YOLO(r"C:\Users\logesh A.J\Documents\projects\farming_rover\main\tomato_disease_best.pt")

running = False
current_model = None
frame_count = {"ripe": 0, "unripe": 0, "diseases": {}}


# ---------------- FUNCTIONS ----------------
def update_status(msg, color="white", hold=3000):
    """Update status label and keep message for at least `hold` ms (default 3s)."""
    status_label.config(text=msg, fg=color)
    root.after(hold, lambda: None)  # keeps message stable for given time


def connect_cam():
    try:
        response = requests.get(CAM_URL, timeout=1)
        if response.status_code == 200:
            return True
    except:
        
        return False
    return False


def run_detection(model_choice):
    global running, current_model

    if model_choice == "ripe":
        current_model = MODEL1
        heading_label.config(text="🍅 Ripeness Detection")
    elif model_choice == "disease":
        current_model = MODEL2
        heading_label.config(text="🌿 Disease Detection")

    while running:
        if not connect_cam():
            update_status("❌ Camera not connected", "red")
            time.sleep(1)
            continue

        try:
            response = requests.get(CAM_URL, timeout=5)
            frame_bytes = response.content
            img = cv2.imdecode(np.frombuffer(frame_bytes, np.uint8), cv2.IMREAD_COLOR)

            if img is None:
                update_status("⚠️ Failed to decode frame", "yellow")
                continue

            results = current_model(img, verbose=False)
            annotated = results[0].plot()

            # Resize frame (medium size)
            annotated = cv2.resize(annotated, (800, 500), interpolation=cv2.INTER_LINEAR)

            # Convert OpenCV BGR to Tkinter-compatible image
            img_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(image=img_pil)

            video_label.config(image=img_tk)
            video_label.image = img_tk  # keep reference

            # Count detections
            for box in results[0].boxes:
                cls_name = results[0].names[int(box.cls)]
                if model_choice == "ripe":
                    if cls_name.lower() == "ripe":
                        frame_count["ripe"] += 1
                    else:
                        frame_count["unripe"] += 1
                elif model_choice == "disease":
                    frame_count["diseases"][cls_name] = frame_count["diseases"].get(cls_name, 0) + 1

            update_status("✅ Running Detection", "green")

        except Exception as e:
            update_status(f"⚠️ Error: {e}", "red")

        time.sleep(1)

    update_status("🛑 Detection stopped", "red")


def start_model(choice):
    global running
    stop_model()  # ensure previous one stops before starting new
    running = True
    threading.Thread(target=run_detection, args=(choice,), daemon=True).start()
    update_status("⌛ Initializing model...", "yellow")
    root.after(2000, lambda: update_status("✅ Model Ready", "green"))


def stop_model():
    global running
    running = False
    update_status("🛑 Stopping model...", "red")


def show_status():
    if current_model == MODEL1:
        msg = f"Ripe: {frame_count['ripe']} | Unripe: {frame_count['unripe']}"
    elif current_model == MODEL2:
        total = sum(frame_count["diseases"].values())
        msg = f"Disease Counts: {frame_count['diseases']} | Total={total}"
    else:
        msg = "No model running"
    update_status(msg, "white")


# ---------------- UI ----------------
root = tk.Tk()
root.title("Smart Farming Rover Dashboard")
root.configure(bg="black")
root.state("zoomed")  # Fullscreen

# Heading
heading_label = tk.Label(root, text="Select Detection Mode", font=("Arial", 28, "bold"), fg="red", bg="black")
heading_label.pack(pady=20)

# Video Display Area (no width/height here)
video_label = tk.Label(root, bg="black")
video_label.pack(pady=10)

# Status
status_frame = tk.Frame(root, bg="black", highlightthickness=2, highlightbackground="red")
status_frame.pack(fill="x", pady=10, padx=50)

status_label = tk.Label(status_frame, text="Waiting for action...", font=("Arial", 16), fg="white", bg="black")
status_label.pack(pady=5)

# Buttons (always visible at bottom)
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(side="bottom", pady=30)

btn_ripeness = tk.Button(btn_frame, text="Ripeness Detection", font=("Arial", 16, "bold"),
                         bg="red", fg="white", width=20, command=lambda: start_model("ripe"))
btn_ripeness.grid(row=0, column=0, padx=20)

btn_disease = tk.Button(btn_frame, text="Disease Detection", font=("Arial", 16, "bold"),
                        bg="red", fg="white", width=20, command=lambda: start_model("disease"))
btn_disease.grid(row=0, column=1, padx=20)

btn_stop = tk.Button(btn_frame, text="Stop", font=("Arial", 16, "bold"),
                     bg="red", fg="white", width=20, command=stop_model)
btn_stop.grid(row=0, column=2, padx=20)

btn_status = tk.Button(btn_frame, text="Status", font=("Arial", 16, "bold"),
                       bg="red", fg="white", width=20, command=show_status)
btn_status.grid(row=0, column=3, padx=20)

root.mainloop()
