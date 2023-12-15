from cap_from_youtube import cap_from_youtube
import os
import cv2
import time

character = "█" # @#$█W

def print_image(image):
	image = cv2.resize(image, (os.get_terminal_size().columns, os.get_terminal_size().lines))
	line = "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image])
	print(line)

url = "https://www.youtube.com/watch?v=ZQAvj5rdgtY"
vid = cap_from_youtube(url, "1440p60")

# vid = cv2.VideoCapture(best.url)
fps = vid.get(cv2.CAP_PROP_FPS)

try: 
	while True:
		ret, frame = vid.read()
		if not ret:
			break

		print_image(frame)

		time.sleep(1/fps)
finally:
	vid.release() 
	print("\033[0m")
