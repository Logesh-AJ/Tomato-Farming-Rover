from ultralytics import YOLO
import cv2
import os
from datetime import datetime

# ============================
# 🔧 CONFIGURE YOUR INPUT HERE
# ============================
SOURCE = r"C:\Users\logesh A.J\Documents\projects\farming_rover\main\test_imag_diseases\Mosaic virus\WhatsApp Image 2025-08-13 at 00.02.59_82770793.jpg"  # Image path
#SOURCE = r"http://localhost:8000/test_1.mp4" # Video path
#SOURCE = 0             
# # Webcam (0 = default camera)

# ============================
# 🔧 MODEL PATH
# ============================
MODEL_PATH = r"C:\Users\logesh A.J\Documents\projects\farming_rover\main\tomato_disease_best.pt"  # YOLOv8 trained model path
SAVE_DIR = r"C:\Users\logesh A.J\Documents\projects\farming_rover\main\runs_diseases"                  # Folder to save outputs
os.makedirs(SAVE_DIR, exist_ok=True)

model = YOLO(MODEL_PATH)

# ============================
# 📸 SOURCE TYPE HANDLER
# ============================
is_webcam = isinstance(SOURCE, int) or (isinstance(SOURCE, str) and SOURCE.isdigit())
source_valid = True

if is_webcam:
    print("[INFO] Starting webcam detection...")
    cap = cv2.VideoCapture(int(SOURCE))
    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        source_valid = False

    while source_valid:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] Webcam frame not received. Exiting.")
            break

        results = model.predict(source=frame, stream=True)
        for r in results:
            annotated_frame = r.plot()

        cv2.imshow("YOLOv8 - Webcam Detection", annotated_frame)

        # Save snapshot
        filename = os.path.join(SAVE_DIR, f"webcam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

elif isinstance(SOURCE, str) and os.path.isfile(SOURCE):
    ext = os.path.splitext(SOURCE)[1].lower()

    if ext in ['.jpg', '.jpeg', '.png']:
        print("[INFO] Running detection on image...")
        results = model.predict(source=SOURCE)
        annotated_img = results[0].plot()
        cv2.imshow("YOLOv8 - Image Detection", annotated_img)
        filename = os.path.join(SAVE_DIR, f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, annotated_img)
        print(f"[RESULT] Image saved at: {filename}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif ext in ['.mp4', '.avi', '.mov']:
        print("[INFO] Running detection on video...")
        cap = cv2.VideoCapture(SOURCE)
        if not cap.isOpened():
            print("[ERROR] Could not open video.")
        else:
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            output_file = os.path.join(SAVE_DIR, f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                results = model.predict(source=frame, stream=True)
                for r in results:
                    annotated_frame = r.plot()

                out.write(annotated_frame)
                cv2.imshow("YOLOv8 - Video Detection", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()
            print(f"[RESULT] Video saved at: {output_file}")
    else:
        print(f"[ERROR] Unsupported file type: {ext}")
else:
    print(f"[ERROR] Invalid source or file not found: {SOURCE}")
