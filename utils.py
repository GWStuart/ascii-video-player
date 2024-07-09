from time import sleep, time
from cap_from_youtube import cap_from_youtube
from os import system, get_terminal_size
from ffpyplayer.player import MediaPlayer
import keyboard
import cv2


character = "█" # @#█$
# ascii_gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
# ascii_gradient = "@0r,."
# ascii_gradient = "@0r,. "
ascii_gradient = "@%#*+=-:. "

def _image_fit_to_screen(image):
    # Returns the image resized fit to terminal dimensions
    # Will distort the image
    return cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    
def _image_fit_to_columns(image):
    # Returns the image resized fit the number of terminal columns 
    rows, columns, _ = image.shape
    terminal_columns = get_terminal_size().columns
    num_rows = round((terminal_columns / columns) * rows)
    return cv2.resize(image, (terminal_columns, num_rows))

def _image_best_fit(image):
    # Returns the image resized to the largest size without changing ratio 
    rows, columns, _ = image.shape
    ratio = rows / columns
    terminal_columns, terminal_rows = get_terminal_size().columns, (get_terminal_size().lines - 1) * 2
    num_columns = round(min(terminal_columns, terminal_rows / ratio))
    return cv2.resize(image, (num_columns, int(num_columns * ratio * 0.5)))

def _render_colour(image):
    # print("\033[H" + "".join("".join(f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row) for row in image), end='')
    print("\033[H", end="")
    for row in image:
        for pixel in row:
            print(f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}", end="")

def _render_grayscale(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("\033[H", end="")
    for row in image:
        for pixel in row:
            print(f"\033[38;2;{pixel};{pixel};{pixel}m{character}", end="")

def _render_ascii_gradient(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("\033[H", end="")
    for row in image:
        for pixel in row:
            character = ascii_gradient[round(pixel / 255 * (len(ascii_gradient) - 1))] 
            print(character, end="")
            # print(f"\033[38;2;{pixel};{pixel};{pixel}m{character}", end="")

def _ascii_end():
    # print(f"\033[{get_terminal_size().lines - 1};{get_terminal_size().columns}H")
    print("\033[0m")

def print_image(path, grayscale=False, ascii_gradient=False, image_fit=1):
    # image_fit: 1 -> defaults fit to screen, 2 -> fit to terminal columns, 3 -> best fit to terminal
    image = cv2.imread(path)
    if image_fit == 1:
        image = _image_fit_to_screen(image)
    elif image_fit == 2:
        image = _image_fit_to_columns(image)
    else:
        image = _image_best_fit(image)
    
    if grayscale:
        _render_grayscale(image)
    elif ascii_gradient:
        _render_ascii_gradient(image)
    else:
        _render_colour(image)

    _ascii_end()

def play_video(url): # plays a youtube video for the given url
    vid = cap_from_youtube(url, "144p")  # maybe allow changing of resolution
    fps = vid.get(cv2.CAP_PROP_FPS)

    try:
        while True:
            ret, frame = vid.read()
            if not ret:
                break

            if keyboard.is_pressed("q"):
                break

            _render_colour(frame)

            sleep(1/fps)

    finally:
        vid.release() 
        _ascii_end()


def play_mp4(path):
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

            if keyboard.is_pressed("q"):
                break

            _render_colour(frame)

            sleep(1/fps)
    finally:
        vid.release() 
        _ascii_end()

def view_camera():
    vid = cv2.VideoCapture(0)

    try:
        fps = 10  # maybe allow the user to customise this later
        prev = 0

        while True:
            time_elapsed = time() - prev
            ret, frame = vid.read()

            if keyboard.is_pressed("q"):
                break

            if time_elapsed > 1/fps:
                prev = time()

                frame = _image_fit_to_screen(frame)
                _render_colour(frame)
    finally:
        vid.release()
        _ascii_end()
