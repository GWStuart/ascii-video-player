from time import sleep
from os import system, get_terminal_size
import cv2

vid = cv2.VideoCapture("ignored/video/bad_apple.mp4")
fps = vid.get(cv2.CAP_PROP_FPS)

character = "█" # @#█$

def get_image(image):
    image = cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')

try:
    system("cls")
    # print("")
    while True:
        ret, frame = vid.read()
        if not ret:
            break

        frame = get_image(frame)
        print("\033[H", end="")
        # print(f"\033[{0};{0}H")

        sleep(1/fps)

finally:
    vid.release() 
    print(f"\033[{get_terminal_size().columns};{get_terminal_size().lines - 2}H")
    print("\033[0m")