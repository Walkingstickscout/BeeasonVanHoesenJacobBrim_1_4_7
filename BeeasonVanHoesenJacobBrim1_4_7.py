from __future__ import print_function
import PIL
import matplotlib.pyplot as plt
import os.path 

def picture_alteration(original_image):
    print('What alteration would you like to do to the picture?', '\n')
    alteration=['RoundCorners', 'Frame', 'CornerCut', 'Swirl', 'ColorChange', 'AddText', 'AddShape']
    for a in alteration[:len(alteration)]:
        print(a+'\n')
    width, height = original_image.size
    if raw_input() == 'RoundCorners':
        radius = int(raw_input('Radius:'))