from argparse import ArgumentParser, RawDescriptionHelpFormatter
from sys import argv
from utils import *
import subprocess

description = """
A terminal video player written in python

Usage:
render "camera"  --> attempts to access your camera and shows you the output
render image.png --> renders the image. Currently only supports png and jpg files
render video.mp4 --> plays the mp4 video. Can be combined with the -m flag to play mute
render hhtps://  --> renders a youtube video given its url
"""

epilog = """
Developed by GWStuart
See GitHub page: https://github.com/GWStuart/ascii-video-player
"""

# Supported image formats
IMAGE_FORMATS = ("png", "jpg", "jpeg", "webp")

parser = ArgumentParser(prog="render", description=description, formatter_class=RawDescriptionHelpFormatter, epilog=epilog)

parser.add_argument("file", nargs="?", help="file to render")
parser.add_argument("-g", "--gray-scale", action="store_true", help="render in grayscale")
parser.add_argument("-a", "--ascii-gradient", action="store_true", help="render using an ascii gradient")
parser.add_argument("-m", "--mute", action="store_true", help="for videos, play file in mute")
parser.add_argument("-c", "--columns-fit", action="store_true", help="fit image to termianl screen horiztonally without distorting image")
parser.add_argument("-b", "--best-fit", action="store_true", help="resize image for best fit without distorting image")

args = parser.parse_args()

if args.file:
    subprocess.run(["tput", "smcup"])
    image_fit = 2 if args.columns_fit else 3 if args.best_fit else 1

    if args.file == "camera":
        view_camera(grayscale=args.gray_scale, ascii_gradient=args.ascii_gradient, image_fit=image_fit)
    elif args.file[:5] == "https":
        play_video(args.file)
    else:
        extension = args.file[args.file.index(".") + 1:]
        if extension in IMAGE_FORMATS:
            print_image(args.file, grayscale=args.gray_scale, ascii_gradient=args.ascii_gradient, image_fit=image_fit)
        elif extension in ["mp4"]:
            play_mp4(args.file)
        else:
            print(f"unsupported file: {extension}")

    input("press enter to continue")
    subprocess.run(["tput", "rmcup"])
else:
    parser.print_help()

