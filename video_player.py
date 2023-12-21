from time import sleep
from os import system
import cv2
from utils import *

vid = cv2.VideoCapture("ignored/video/bad_apple.mp4")
fps = vid.get(cv2.CAP_PROP_FPS)

try:
    while True:
        ret, frame = vid.read()
        if not ret:
            break

        print_image(frame)

        sleep(1/fps)
finally:
    vid.release() 
    ascii_end()