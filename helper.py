import os
import sys
from PIL import Image, ImageDraw

def make_rounded_image(image_path, size=(250, 250), radius=125):
    # Open the image and resize it
    img = Image.open(image_path).resize(size, Image.LANCZOS)
    
    # Create a mask for the rounded corners
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
    # Apply the mask to the image
    rounded_image = Image.new("RGB", size)
    rounded_image.paste(img, (0, 0), mask)
    return rounded_image

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path,relative_path)
