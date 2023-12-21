from time import time
import cv2
from utils import *

vid = cv2.VideoCapture(0)

try:
	fps = 10
	prev = 0

	while True:
		time_elapsed = time() - prev
		ret, frame = vid.read()

		if time_elapsed > 1/fps:
			prev = time()

			print_image(frame)
finally:
    vid.release()
    ascii_end()
