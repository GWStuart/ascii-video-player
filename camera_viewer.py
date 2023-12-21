from time import sleep, time
from os import system, get_terminal_size
import cv2

vid = cv2.VideoCapture(0)

character = "█" # @#█$

def print_image(image):
    image = cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("\033[H" + "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')


try:
	system("cls")

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
    print(f"\033[{get_terminal_size().columns};{get_terminal_size().lines - 2}H")
    print("\033[0m")
