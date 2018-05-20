# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:22:09 2018

@author: Vijesh
"""
import shutil
from os import listdir
import os
import tqdm

filenames = listdir('D:/TUHH/Arbeit/refinenet-master/refinenet-master/datasets/cocostuff_ship_bckg/val_imgs')
for f in tqdm.tqdm(filenames):
    jpg_file = f.replace('png','jpg')
    full_path = os.path.join('D:/TUHH/Arbeit/Data/val2017/val2017',jpg_file)
    shutil.copy(full_path,'D:/TUHH/Arbeit/Data/val2017_coco')
    