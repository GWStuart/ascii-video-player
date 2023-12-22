from time import sleep, time
from cap_from_youtube import cap_from_youtube
from os import system, get_terminal_size
from ffpyplayer.player import MediaPlayer
import keyboard
import cv2


character = "█" # @#█$

def _print_ascii(image):
    image = cv2.resize(image, (get_terminal_size().columns, get_terminal_size().lines - 1))
    print("\033[H" + "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m{character}" for pixel in row]) + "\n" for row in image]), end='')

def _ascii_end():
	print(f"\033[{get_terminal_size().lines - 1};{get_terminal_size().columns}H")
	print("\033[0m")

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

			_print_ascii(frame)

			sleep(1/fps)

	finally:
		vid.release() 
		_ascii_end()

def print_image(path):
	image = cv2.imread(path)

	_print_ascii(image)
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

	        _print_ascii(frame)

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

				_print_ascii(frame)
	finally:
	    vid.release()
	    _ascii_end()