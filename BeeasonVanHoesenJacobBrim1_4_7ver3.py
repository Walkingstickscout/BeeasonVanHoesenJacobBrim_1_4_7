from __future__ import print_function
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import os.path
from PIL import ImageDraw

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
    alteration=['RoundCorners', 'Frame', 'CornerCut', 'Swirl', 'ColorChange', 'AddText', 'AddShape']
    for a in alteration[:len(alteration)]:
        print(a+'\n')
    width, height = im.size
    if raw_input('Choice: ') == 'RoundCorners':
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
    elif raw_input('Choice: ') == 'Frame':
        thickness = int(raw_input('Thickness: '))
        draw = ImageDraw.Draw(im)
        draw.line((width, height) + im.size, fill=128)
        result = PIL.Image.new('RGBA', im.size, (0,0,0,0))
        result.paste(im, (0,0))
        new_image_filename = os.path.join(new_directory, original_image + '.png')
        result.save(new_image_filename)
        print('You will find the new picture in ', new_directory)