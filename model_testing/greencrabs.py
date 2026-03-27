###(base) C:\Users\gviei> conda activate rov-vision
##(rov-vision) C:\Users\gviei> cd C:\Users\gviei\OneDrive\Documents\rov-vision\scripts
###(rov-vision) C:\Users\gviei\OneDrive\Documents\rov-vision> python greencrabs.py


###imports libraries 
from ultralytics import YOLO
from pathlib import Path
from collections import Counter


##gets me to the project directory folder so python knows where to look
ROOT = Path(r"C:\Users\gviei\OneDrive\Documents\rov-vision")

##loads in trained YOLOv8 model into variable
model = YOLO(ROOT / "runs" / "detect" / "train" / "weights" / "best.pt")

#sets desired image paths to a variable, these just happen to be the paths that I was last using
#image_path1 = ROOT / "images" / "rock.jpg"
image_path2 = ROOT / "images" / "green.jpg"
#image_path3 = ROOT / "images" / "jonah.png"

##runs model (with .1 confidence interval) var against image path var, tells it to save as an image
#results = model(image_path1, save=True, conf=0.1)
results = model(image_path2, save=True, conf=0.1)
#results = model(image_path3, save=True, conf=0.1)

#store first element in results as var r
r = results[0]

#sorts the boxes into a list
class_ids = r.boxes.cls.tolist()

#creates name dictionary
names = r.names

#counts how many instances of each box and after converting them into integers
counts = Counter(names[int(i)] for i in class_ids)

print("\n\nThe numbers of each crab in this image are:")

#loops through the name list and prints the amount of each crab there is
for name in names.values():
    print(f"{name}: {counts.get(name, 0)}")

#foolproof way for me to remember where the photos that the model ran on are
print("Saved to:", results[0].save_dir)
