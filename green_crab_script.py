## this also just takes pictures and saves them to a directory
## i used picam2 library for this one as opposed to picamzero

from picamera2 import Picamera2, Preview
import time
import os

#set directory of where i want photos as a variable
home_dir = os.path.expanduser("~/Documents/crab_pics/green_crabs")

#creates the photo location in the directory and names them "green_crab_ current timestamp .jpg"
photo_location = f"{home_dir}/green_crab_{int(time.time())}.jpg"

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (1280,720)})
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()

# i find seven second delay to be the perfect amount of time to snap a pic
time.sleep(7)

#stores photo in the photo directory
picam2.capture_file(photo_location)

##supposedly stops my picam from crashing, i keep running into cpp errors 1500,1501 and 1502
picam2.stop_preview()
picam2.stop()
picam2.close()

print(f"your photo is stored at {photo_location}")
                                        
