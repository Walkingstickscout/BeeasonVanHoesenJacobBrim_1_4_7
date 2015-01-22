from __future__ import print_function
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import os.path
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np

def picture_alteration(original_image, directory=None):
    '''Choose one of the choices and type it out exactly how
    it is seen, cases included
    The file you choose has to be in the working directory or this will not work'''
    if directory == None:
        directory = os.getcwd()
        if directory != 'modified':#If the current working directory is named Modified, the image will be edited here
            new_directory = os.path.join(directory, 'modified')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass
    else:
        new_directory = directory
    im = Image.open(original_image)#makes it so the image can be viewed by PIL
    print('What alteration would you like to do to the picture?', '\n')
    alteration=['RoundCorners', 'Frame', 'Crop', 'ColorChange', 'AddText', 'AddEllipse']
    for a in alteration[:len(alteration)]:
        print(a+'\n')
    width, height = im.size
    img = plt.imread(original_image)#Makes it so the image can be viewed by plt
    choice = raw_input('Choice: ')
    if choice == 'RoundCorners':#Rounds the corners to a certain radius
        radius = int(raw_input('Radius: '))
        rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
        drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
        drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
        drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))
        drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255))
        drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255))
        drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255))
        drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255))
        result = PIL.Image.new('RGBA', im.size, (0,0,0,0))
        result.paste(im, (0,0), mask=rounded_mask)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        result.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
        del result
    elif choice == 'Frame':#Puts a color frame of the users choice around the image
        thickness = int(raw_input('Thickness: '))
        fill = raw_input('Color Fill: ')
        borderedImage = ImageOps.expand(im ,border=thickness, fill=fill)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        borderedImage.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'Crop':#Crops the image to where the user wants
        left = int(raw_input('Left: '))
        right = int(raw_input('Right: '))
        upper = int(raw_input('Upper: '))
        lower = int(raw_input('Lower: '))
        cropped_image = im.crop((left, upper, right, lower))
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        cropped_image.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'ColorChange':#changes the color of a selcetion of the image to a certain image
        draw = ImageDraw.Draw(im)
        x1 = int(raw_input('Row 1: '))
        x2 = int(raw_input('Row 2: '))
        y1 = int(raw_input('Column 1: '))
        y2 = int(raw_input('Column 2: '))
        red = int(raw_input('Red Value: '))
        blue = int(raw_input('Blue Value: '))
        green = int(raw_input('Green Value: '))
        selection = (x1, y1, x2, y2)
        new_color = (red, green, blue)
        draw.rectangle(selection, fill=new_color)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        im.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'AddText':#Adds a text that the user places of a certain color that is chosen by the user
        text = (raw_input('Text: '))
        red = int(raw_input('Red Value: '))
        green = int(raw_input('Green Value: '))
        blue = int(raw_input('Blue Value: '))
        x = int(raw_input('X Value: '))
        y = int(raw_input('Y Value: '))
        size = int(raw_input('Font Size: '))
        draw = ImageDraw.Draw(im)
        font1 = ImageFont.truetype("arial.ttf", size)
        draw.text((x, y), text, fill=(red, green, blue), font=font1)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        im.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'AddEllipse':#Adds an oval shape of a chosen color to a place chosen by the user
        x1 = int(raw_input('First X:'))
        x2 = int(raw_input('Second X:'))
        y1 = int(raw_input('First Y:'))
        y2 = int(raw_input('Second Y:'))
        outRed = int(raw_input('Outline Red: '))
        outGreen = int(raw_input('Outline Green: '))
        outBlue = int(raw_input('Outline Blue: '))
        fillRed = int(raw_input('Fill Red: '))
        fillGreen = int(raw_input('Fill Green: '))
        fillBlue = int(raw_input('Fill Blue: '))
        coords = (x1, y1, x2, y2)
        fill = (fillRed, fillGreen, fillBlue)
        outline = (outRed, outGreen, outBlue)
        draw = ImageDraw.Draw(im)
        draw.ellipse(coords, fill=fill, outline=outline)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        im.save(new_image_filename)
        print('You will find the new picture in ', new_directory)