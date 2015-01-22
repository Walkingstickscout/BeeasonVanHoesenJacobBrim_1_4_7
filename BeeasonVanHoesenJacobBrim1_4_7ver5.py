from __future__ import print_function
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import os.path
from PIL import ImageOps
from PIL import ImageDraw
import numpy as np

def picture_alteration(original_image, directory=None):
    if directory == None:
        directory = os.getcwd()
        new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    im = Image.open(original_image)
    print('What alteration would you like to do to the picture?', '\n')
    alteration=['RoundCorners', 'Frame', 'Crop', 'ColorChange', 'AddText', 'AddShape']
    for a in alteration[:len(alteration)]:
        print(a+'\n')
    width, height = im.size
    img = plt.imread(original_image)
    choice = raw_input('Choice: ')
    if choice == 'RoundCorners':
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
    elif choice == 'Frame':
        thickness = int(raw_input('Thickness: '))
        fill = raw_input('Color Fill: ')
        borderedImage = ImageOps.expand(im ,border=thickness, fill=fill)
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        borderedImage.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'Crop':
        left = int(raw_input('Left: '))
        right = int(raw_input('Right: '))
        upper = int(raw_input('Upper: '))
        lower = int(raw_input('Lower: '))
        cropped_image = im.crop((left, upper, right, lower))
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        cropped_image.save(new_image_filename)
        print('You will find the new picture in ', new_directory)
    elif choice == 'ColorChange':
        height2 = len(img)
        width2 = len(img[0])
        row1 = int(raw_input('Row 1: '))
        row2 = int(raw_input('Row 2: '))
        column1 = int(raw_input('Column 1: '))
        column2 = int(raw_input('Column 2: '))
        red = int(raw_input('Red Value: '))
        blue = int(raw_input('Blue Value: '))
        green = int(raw_input('Green Value: '))
        for row in range(row1, row2):
            for column in range(column1, column2):
                new_color = [red, green, blue]
                current_color = original_image.getpixel( (row, column) )
                colored_image = original_image.putpixel( (row, column), new_color )
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        colored_image.save(new_image_filename)
        