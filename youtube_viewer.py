from cap_from_youtube import cap_from_youtube
from time import sleep
from os import system, get_terminal_size
import cv2

colour = True
gradient = " .;w$"
character = "█" # @#$█W

def print_image(image):
    image = cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("\033[H" + "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')

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
    print(f"\033[{get_terminal_size().columns};{get_terminal_size().lines - 2}H")
    print("\033[0m")
