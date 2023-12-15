import cv2
import os
import timeit

def print_image(image):
	image = cv2.resize(image, (os.get_terminal_size().columns, os.get_terminal_size().lines))
	line = "".join(["".join([f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m$" for pixel in row]) + "\n" for row in image])
	print(line + "\033[0m")


image = cv2.imread("ignored/images/image1.jpg")

# print(os.get_terminal_size())
print_image(image)
# print(timeit.timeit(lambda: print_image(image), number=100))

'''
test 1: 6.519621799991
test 2: 5.718865399991046 <--> 6.01
test 3: 5.455661300002248 <--> 5.468270000012126
test 4: 5.373860399995465
'''