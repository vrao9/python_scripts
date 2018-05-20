from os import listdir
from PIL import Image
import numpy as np
import tqdm

class_idx = np.zeros(183)
file_names = listdir('D:/TUHH/Arbeit/Data/stuffthingmaps_trainval2017/train2017')
img_counter = 0

for img_name in tqdm.tqdm(file_names):
    img = Image.open("D:/TUHH/Arbeit/Data/stuffthingmaps_trainval2017/train2017/" + img_name)
    data = np.array( img, dtype='uint8')
    unique = np.unique(data)
    if 8 in unique:
        modified_img = np.zeros(data.shape)
        for i in unique:
            temp = data == i
            if i == 4:
                modified_img[temp] = 1
            elif i == 1:
                modified_img[temp] = 2
            elif i == 15:
                modified_img[temp] = 3
            elif i == 8:
                modified_img[temp] = 4
            elif i == 43:
                modified_img[temp] = 5
            elif i == 5:
                modified_img[temp] = 6 
            elif i == 2:
                modified_img[temp] = 7  
            elif i == 16:
                modified_img[temp] = 8                
            elif i == 61:
                modified_img[temp] = 9 
            elif i == 20:
                modified_img[temp] = 10                
            elif i == 66:
                modified_img[temp] = 11               
            elif i == 17:
                modified_img[temp] = 12               
            elif i == 18:
                modified_img[temp] = 13               
            elif i == 3:
                modified_img[temp] = 14               
            elif i == 0:
                modified_img[temp] = 15               
            elif i == 63:
                modified_img[temp] = 16 
            elif i == 19:
                modified_img[temp] = 17               
            elif i == 62:
                modified_img[temp] = 18               
            elif i == 6:
                modified_img[temp] = 19
            elif i == 71:
                modified_img[temp] = 20  
            elif i == 255:
                modified_img[temp] = 255                
            else:
                modified_img[temp] = 0
        modified_img1 = modified_img.astype(dtype = 'uint8')
        mod_img = Image.fromarray(modified_img1)
        
        mod_img.save('D:/TUHH/Arbeit/Data/coco/train_modified_coco_for_voc/'+img_name)

