##conversionn of best.pt file to openvino model file
#as a result of pytorch not working on rpi4b, i need to use openvino instead

from ultralytics import YOLO
model = YOLO("runs/detect/crabv3_gpu/weights/best.pt")
model.export(format = "openvino", imgsz = 640)
print("the conversion worked")
