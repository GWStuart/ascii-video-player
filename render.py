from argparse import ArgumentParser, RawDescriptionHelpFormatter
from sys import argv
from utils import *

description = """
A terminal video player written in python

Usage:
render "camera"  --> attempts to access your camera and shows you the output
render image.png --> renders the image. Currently only supports png and jpg files
render video.mp4 --> plays the mp4 video. Can be combined with the -m flag to play mute
render hhtps://  --> renders a youtube video given its url
"""

parser = ArgumentParser(prog="render", description=description, formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("file", nargs="?", help="file to render")
parser.add_argument("-g", "--gray-scale", action="store_true", help="render in grayscale")
parser.add_argument("-m", "--mute", action="store_true", help="play file in mute")

args = parser.parse_args()

if args.file:
	if args.file == "camera":
		view_camera()
	elif args.file[:5] == "https":
		play_video(args.file)
	else:
		extension = args.file[-3:]
		if extension in ["png", "jpg"]:
			print_image(args.file)
		elif extension in ["mp4"]:
			play_mp4(args.file)
		else:
			print(f"unsupported file")
else:
    parser.print_help()
