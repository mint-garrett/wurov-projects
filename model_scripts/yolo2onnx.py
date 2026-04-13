##conversionn of best.pt file to openvino model file
#as a result of pytorch not working on rpi4b, i need to use openvino instead

from ultralytics import YOLO
model = YOLO("wurov-projects-main/pi_py_stream/best.pt")
model.export(
    format = "onnx", 
    imgsz = 640,
    simplify = True,
    dynamic = False
    )
print("the conversion worked")