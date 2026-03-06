##access picamera2 camera
##basically same thing as regular computer just switch cv2 functions with picam2 functions

from picamera2 import Picamera2
import cv2

picam2 = Picamera2()
picam2.start()

win_name = 'opencv preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    frame = picam2.capture_array()
    if frame is None:
        break
    cv2.imshow(win_name, frame)

picam2.stop()
cv2.destroyAllWindows()
