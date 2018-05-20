# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 12:20:51 2018

@author: Vijesh
"""

from os import listdir

filenames = listdir('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/JPEGImages_boat_train/')
with open("D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/ImageSets/Segmentation/train.txt", "w") as a:
    for file in filenames:
        a.write(str(file)+'\r')