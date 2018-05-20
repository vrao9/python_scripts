import os
from PIL import Image
import numpy as np
import tqdm
import shutil

file_names = os.listdir('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass')


for img_name in tqdm.tqdm(file_names):
    img = Image.open('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass/' + img_name)
    data = np.array( img, dtype='uint8')
    unique = np.unique(data)
    if 4 in unique:
        full_path = os.path.join('D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass/',img_name)
        shutil.copy(full_path,'D:/TUHH/Arbeit/Data/VOCdevkit/voc2012_trainval/SegmentationClass_boat')