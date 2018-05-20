from os import listdir
from PIL import Image
import numpy as np
import tqdm

class_idx = np.zeros(183)
file_names = listdir('D:/TUHH/Arbeit/Data/stuffthingmaps_trainval2017/val2017')
img_counter = 0

for img_name in tqdm.tqdm(file_names):
    img = Image.open("D:/TUHH/Arbeit/Data/stuffthingmaps_trainval2017/val2017/" + img_name)
    data = np.array( img, dtype='uint8')
    unique = np.unique(data)
    if 8 in unique:
        modified_img = np.zeros(data.shape)
        for i in unique:
            temp = data == i
            if i == 8:
                modified_img[temp] = 1
            elif i == 255:
                modified_img[temp] = 255
            else:
                modified_img[temp] = 0
        modified_img1 = modified_img.astype(dtype = 'uint8')
        mod_img = Image.fromarray(modified_img1)
        
        mod_img.save('D:/TUHH/Arbeit/Data/val_modified_boat+bckg/'+img_name)

