# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:13:01 2018

@author: Vijesh
"""
import operator
import numpy as np
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)




class_info = open('D:/TUHH/Arbeit/Data/coco/cocostuff_master/cocostuff-labels_edited.txt','r')
x = class_info.readlines()
class_info.close()

class_nums = [int(n.split()[0]) for n in x]
class_labels = [n.split()[1] for n in x] 
del class_labels[0]
class_nums = np.delete(class_nums,(-1),axis = 0)

# create a dictionary of labels
my_dic_coco = {}
for a,b in zip(class_nums, class_labels):
    my_dic_coco[b] = a
#sort dictionary
#my_dic = sorted(my_dic.items(), key=operator.itemgetter(1))
    
#find keys based on values
#print(list(my_dic.keys())[list(my_dic.values()).index(16)])
    
# check if every elements are present or not
'''
for i in range(0,182):
print(list(my_dic_coco.keys())[list(my_dic_coco.values()).index(i)])
'''