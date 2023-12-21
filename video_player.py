from time import sleep
from os import system
import cv2
from ffpyplayer.player import MediaPlayer
from utils import *

path = "ignored/video/crab_rave.mp4"
vid = cv2.VideoCapture(path)
audio = MediaPlayer(path)

fps = vid.get(cv2.CAP_PROP_FPS)

try:
    while True:
        ret, frame = vid.read()
        audio_frame, val = audio.get_frame()
        if not ret:
            break
        if val != 'eof' and audio_frame is not None:
            #audio (idk what this does)
            img, t = audio_frame

        print_image(frame)

        sleep(1/fps)
finally:
    vid.release() 
    ascii_end()