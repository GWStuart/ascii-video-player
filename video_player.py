from time import sleep
from os import system, get_terminal_size
import cv2

vid = cv2.VideoCapture("ignored/video/bad_apple.mp4")
fps = vid.get(cv2.CAP_PROP_FPS)

character = "█" # @#█$

def print_image(image):
    image = cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("\033[H" + "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')

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
    print(f"\033[{get_terminal_size().columns};{get_terminal_size().lines - 2}H")
    print("\033[0m")