from cap_from_youtube import cap_from_youtube
from time import sleep
from os import system
import cv2
from utils import *

# url = "https://www.youtube.com/watch?v=ZQAvj5rdgtY"
url = "https://www.youtube.com/watch?v=IcFD5OMwS4Q"

vid = cap_from_youtube(url, "144p")
fps = vid.get(cv2.CAP_PROP_FPS)

try:
    system("cls")

    while True:
        ret, frame = vid.read()
        if not ret:
            break

        print_image(frame)
        
        sleep(1/fps)

finally:
    vid.release() 
    ascii_end()
