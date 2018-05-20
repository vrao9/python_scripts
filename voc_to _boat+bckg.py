# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:54:03 2018
This is used to generate bckg + boat from the voc dataset which can be used for testing
@author: Vijesh
"""

from os import listdir
from PIL import Image
import numpy as np
import tqdm


file_names = listdir('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/JPEGImages_boat_trainval')


for img_name in tqdm.tqdm(file_names):
    png_file = img_name.replace('jpg','png')
    img = Image.open("D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass/" + png_file)
    data = np.array( img, dtype='uint8')
    unique = np.unique(data)
    if 4 in unique:
        modified_img = np.zeros(data.shape)
        for i in unique:
            temp = data == i
            if i == 4:
                modified_img[temp] = 1
            elif i == 255:
                modified_img[temp] = 255
            else:
                modified_img[temp] = 0
        modified_img1 = modified_img.astype(dtype = 'uint8')
        mod_img = Image.fromarray(modified_img1)
        
        mod_img.save('D:/TUHH/Arbeit/Data/voc_to_boat+bckg_trainval/'+png_file)

