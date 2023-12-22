from argparse import ArgumentParser, RawDescriptionHelpFormatter
from sys import argv
from utils import *

description = """
A terminal video player written in python
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
