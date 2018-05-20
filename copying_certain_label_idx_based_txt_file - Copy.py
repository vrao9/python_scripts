import os
from PIL import Image
import numpy as np
import tqdm
import shutil

file_names = open('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/ImageSets/Segmentation/trainval.txt','r')
lines = file_names.readlines()

file_names.close()
img_counter = 0

for img_name in tqdm.tqdm(lines):
    img_name = img_name.strip('\n')
    img = Image.open('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass/' + img_name + '.png')
    data = np.array( img, dtype='uint8')
    unique = np.unique(data)
    if 4 in unique:
        full_path = os.path.join('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/JPEGImages/',img_name + '.jpg')
        shutil.copy(full_path,'D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/JPEGImages_boat_trainval')