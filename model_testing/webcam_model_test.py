##! conda activate rov-vision
#! cd C:\Users\gviei\OneDrive\Documents\rov-vision\scripts
from ultralytics import YOLO
import cv2
from pathlib import Path

# Load PyTorch model (NOT OpenVINO)
model_path = Path(r"C:\Users\gviei\OneDrive\Documents\rov-vision\runs\detect\crabv42\weights\best.pt")
model = YOLO(str(model_path))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Ultralytics handles everything automatically
    results = model(frame, conf=0.9, imgsz=640, verbose=False)
    annotated_frame = results[0].plot()
    
    cv2.imshow("quick test (PyTorch)", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
