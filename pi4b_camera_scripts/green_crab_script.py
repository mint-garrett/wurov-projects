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

try: ##safety net to make prevent connection error
  preview_config = picam2.create_preview_configuration(main={"size": (1640,1232)})
  picam2.configure(preview_config)
  
  picam2.start_preview(Preview.QTGL)
  
  picam2.start()
  
  # i find seven second delay to be the perfect amount of time to snap a pic
  time.sleep(7)
  
  #stores photo in the photo directory
  picam2.capture_file(photo_location)

finally: 
  picam2.stop_preview()
  picam2.stop()
  picam2.close()

time.sleep(5) ###5 second cooldown window so qtgl window securely closes
print(f"your photo is stored at {photo_location}")
                                        
