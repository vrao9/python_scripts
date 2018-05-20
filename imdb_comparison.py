# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:18:55 2018

@author: Vijesh
"""

from os import listdir
from PIL import Image
import numpy as np
import tqdm
import matplotlib.pyplot as plt


def write_to_txt(total_ratio,file_names):
    cou = np.where((total_ratio >= 0.4) & (total_ratio <=1.0))[0]
    cou_list = list(cou)
    from operator import itemgetter
    new_list = itemgetter(*cou_list)(file_names)
    with open("D:/TUHH/Arbeit/output.txt", "w") as a:
        for file in new_list:
            file = file.strip('.png')
            a.write(str(file)+'\r')

total_ratio = []
path = 'D:/TUHH/Arbeit/refinenet-master/refinenet-master/datasets/cocostuff_ship_bckg/SegmentationClass/'
file_names = listdir(path)

for img_name in tqdm.tqdm(file_names):
    img = Image.open(path + img_name)
    data = np.array( img, dtype='uint8')
    unique, counts = np.unique(data, return_counts=True)
    #print(unique[1])
    ratio = float(counts[1]/data.size)
    total_ratio = np.append(total_ratio,ratio)

np.sort(total_ratio)
mean_of_data = np.mean(total_ratio)
mean_of_data = np.round(mean_of_data,4)

plt.plot(total_ratio,'r.',markersize = 3)
plt.xlabel('No of Images')
plt.ylabel('Ratio of boat to total')
plt.title('coco_dataset_boat_imgs_val')
plt.text(0.1,.950,'mean = ' + str(mean_of_data),fontsize=12)
plt.show()
write_to_txt(total_ratio,file_names)
