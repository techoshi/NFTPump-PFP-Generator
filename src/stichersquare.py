import threading
import sys
from PIL import Image
import argparse
from os import listdir
from os import path

async def stitch(output_dir, filename, img_args, x, y):

    x = threading.Thread(target=saveFile, args=(output_dir,filename,img_args,x,y,))    
    x.start()

    #saveFile(output_dir, filename, img_args, x, y)  
    return True

def saveFile(output_dir, filename, img_args, x, y):
    newImage = Image.new('RGBA', (y, y))
    #newImage = Image.new('RGBA', (x, y))
    #name = "".join(choices(string.ascii_letters, k=5)) + "_"
    brokenPath = ""

    try:
        name = "_"
        for imagePath in img_args:
            brokenPath = imagePath
            if imagePath != None:
                basename = path.basename(imagePath)
                fname = path.splitext(basename)[0]
                name += str(fname) + "_"
                img = Image.open(imagePath)
                if img.mode == "RGB":
                    img = img.convert("RGBA")
                img = img.resize((x, y))
                # newImage.alpha_composite(img)
                width, height = img.size # Get Dimension
                left = (width - y)/2
                top = (height - y)/2
                right = (width + y)/2
                bottom = (height + y)/2

                # Crop the center of the image
                img = img.crop((left, top, right, bottom))
                # width, height = img.size # Get Dimension
               # img = img.resize((width, height))
                newImage.alpha_composite(img.resize((height, height)))
            else:
                name += str(None) + "_"

        if filename == "":
            filename = name
            
        newImage.save(output_dir + filename + ".png") 
        print("minted #" + filename + " for " + output_dir)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")              
        logFile1 = open(output_dir + 'failedStich.txt','a+')
        logFile1.write(filename + " - " + brokenPath + "\n")
        logFile1.close()

    