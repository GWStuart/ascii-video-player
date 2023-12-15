import cv2
import os
import time	

vid = cv2.VideoCapture(0)

def print_image(image):
	image = cv2.resize(image, (os.get_terminal_size().columns, os.get_terminal_size().lines))
	line = "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m$" for pixel in row]) + "\n" for row in image])
	print(line)

try: 
	# while True:  
	# 	ret, frame = vid.read() 

	# 	print_image(frame)

	frame_rate = 10
	prev = 0

	while True:

	    time_elapsed = time.time() - prev
	    ret, frame = vid.read()

	    if time_elapsed > 1./frame_rate:
	        prev = time.time()

	        # Do something with your image here.
	        print_image(frame)
finally:
	vid.release() 
	print("\033[0m")
