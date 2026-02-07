##training script for new dataset that includes the new picam2 pics, as well as the old ones from the internet
##1 activate conda environment
##2  python crabv3_training.py

from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")
    results = model.train(
        data=r"C:\Users\gviei\OneDrive\Documents\rov-vision\datasets\crabs.v3\data.yaml",
        epochs=50, ##how many times the model sees the images
        imgsz=[1640, 1232],##sets the image resolution to the original pic size from the picam2
        batch=-1, ##controls how many images the gpu sees at once, but -1 allows the gpu to decide the safest amount
        rect=True,
        name="crabv3_gpu",
        workers=0,  # windows multiprocessing
        device=0    # force gpu usage
    )
