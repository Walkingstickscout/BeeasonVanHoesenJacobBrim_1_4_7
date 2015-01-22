from __future__ import print_function
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import os.path 

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