# from time import sleep, time
from os import system, get_terminal_size
from cv2 import resize


character = "█" # @#█$

def print_image(image):
    image = resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("\033[H" + "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')

def ascii_end():
	print(f"\033[{get_terminal_size().lines - 1};{get_terminal_size().columns}H")
	print("\033[0m")
