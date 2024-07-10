# An ASCII image viewer and video player
This is a simple python program that can be used to render images with coloured ascii in the terminal.


# Supported image and video formats
- image: png, jpg, webp
- video: mp4
- camera output

# Installation and Configuration
- Clone this repository and cd into it 
- Install the python dependancies using `pip`. The dependancies can be found in the `requirements.txt` file. 
- Test that it has been correctly installed by running `python render.py --help`

Optional:
Create a bash alias so that `render.py` can be run easily from anywhere in the terminal. To do this add something like the line below to your `~/.bashrc`,
```alias render="~/PATH-TO-PROJECT/venv/bin/python ~/PATH-TO-PROJECT/render.py"```

Note that the above command assumes that you are using a python virtual environment. If not then you may need to modify it to just use the system python.

# Usage
See the help page with `render -h`
Render any of the supported files with `render image.png`
View the camera with `render camera`

The output can be modified with several tags:
- "-g" to render image in grayscale
- "-a" to render using an ascii gradient of characters
