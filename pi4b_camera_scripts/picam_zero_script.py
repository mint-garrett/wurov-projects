### this just takes pictures on a picam 2 on a raspberry pi
###not the current one i am using but oh well

from picamzero import Camera
import os
import time

#stores photo folder directory as a string 
home_dir = os.path.expanduser("~/Documents/test_pics") 

#creates dir if it doesn't exist
os.makedirs(home_dir, exist_ok=True)

#names camera function
cam = Camera()

#set cam resolution in px
cam.resolution = (1280,720)

#saves photo as a jpg with the timestamp as part of the name in the home_dir as a variable
photo_location = f"{home_dir}/photo_{int(time.time())}.jpg"

cam.start_preview()
time.sleep(5)
cam.take_photo(photo_location)
cam.stop_preview()

print(f"The photo is stored at {photo_location}")
