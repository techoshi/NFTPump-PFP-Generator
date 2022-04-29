import glob
import json
import asyncio
import os
import threading
from PIL import Image

rootSource = "src/output/WTF/" + "Formatted Output/1of1"
rootOutput = "src/output/WTF/" + "Formatted Output/1of1New/"

listfiles = glob.glob(rootSource + "/*.png")
size = 1640
num = 0

for f1 in listfiles:    
    num = num + 1
    img = Image.open(f1)
    if img.mode == "RGB":
        img = img.convert("RGBA")
    
    width, height = img.size   # Get dimensions
    img = img.resize((width, height))
   
    left = (width - size)/2
    top = (height - size)/2
    right = (width + size)/2
    bottom = (height + size)/2

    # Crop the center of the image
    img = img.crop((left, top, right, bottom))
    newImage = Image.new('RGBA', (1024, 1024))
    newImage.alpha_composite(img.resize((1024, 1024)))
    newImage.save(rootOutput + str(num) + ".png") 