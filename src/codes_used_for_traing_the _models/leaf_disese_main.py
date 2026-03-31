# =============================
# STEP 1: Check GPU Availability (T4)
# =============================
!nvidia-smi

# =============================
# STEP 2: Install Ultralytics YOLOv8
# =============================
!pip install ultralytics --upgrade -q
from ultralytics import YOLO
from google.colab import drive
import os
import torch
import yaml

# Enable CUDA_LAUNCH_BLOCKING for better debugging
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

# =============================
# STEP 3: Mount Google Drive
# =============================
drive.mount('/content/drive', force_remount=True)

# =============================
# STEP 4: Update Class Names in Existing data.yaml
# =============================
dataset_folder = "/content/drive/MyDrive/tomato_ripeness"  # Change to your dataset folder
yaml_path = os.path.join(dataset_folder, "data.yaml")

# Load existing YAML
with open(yaml_path, 'r') as f:
    data_config = yaml.safe_load(f)

# Modify class count and names (ONLY CHANGE HERE)
data_config['nc'] = 9
data_config['names'] = [
    'Early Blight',
    'Healthy',
    'Late Blight',
    'Leaf Miner',
    'Leaf Mold',
    'Mosaic Virus',
    'Septoria',
    'Spider Mites',
    'Yellow Leaf Curl Virus'
]

# Save back the updated YAML
with open(yaml_path, 'w') as f:
    yaml.dump(data_config, f)

print(f"✅ Updated data.yaml at {yaml_path}")
print(data_config)

# =============================
# STEP 5: Prepare Checkpoint Directory
# =============================
checkpoint_dir = "/content/drive/MyDrive/tomato_ripeness_checkpoints"
os.makedirs(checkpoint_dir, exist_ok=True)

custom_checkpoint = os.path.join(checkpoint_dir, "yolov8_tomato_model", "weights", "last.pt")

# =============================
# STEP 6: Load Model (Resume if Checkpoint Exists)
# =============================
if os.path.exists(custom_checkpoint):
    checkpoint_path = custom_checkpoint
    resume_training = True
    print(f"Resuming training from {checkpoint_path}")
    model = YOLO(checkpoint_path)
else:
    checkpoint_path = 'yolov8s.yaml'
    resume_training = False
    print("No checkpoint found; starting with fresh model configuration")
    model = YOLO(checkpoint_path)
    model.nc = 9  # Updated number of classes

print(f"Model number of classes (nc): {model.nc}")

# =============================
# STEP 7: Train the YOLOv8 Model
# =============================
model.train(
    data=yaml_path,
    epochs=50,
    imgsz=640,
    batch=16,
    workers=4,
    val=True,
    patience=15,
    project=checkpoint_dir,
    name="yolov8_tomato_model",
    exist_ok=True,
    save_period=1,
    save=True,
    pretrained=False,
    resume=resume_training
)

# =============================
# STEP 8: Evaluate on Test Set
# =============================
model.val(split='test')

# =============================
# STEP 9: Save Best and Last Models to Google Drive Root (Failsafe)
# =============================
!cp {checkpoint_dir}/yolov8_tomato_model/weights/best.pt /content/drive/MyDrive/
!cp {checkpoint_dir}/yolov8_tomato_model/weights/last.pt /content/drive/MyDrive/

print("✅ Training complete. Models saved to Google Drive.")
