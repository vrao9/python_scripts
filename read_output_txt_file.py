import numpy as np
import matplotlib.pyplot as plt
big_file = open('D:/TUHH/Arbeit/refinenet-master/refinenet-master/cache_data/test_examples_coco/result_20180520155229_predict_custom_data/prediction_scales_1/output.txt', 'r')
acc_boat = []
iou_boat = []
acc_bckg = []
iou_bckg = []
for line in big_file:
   if 'class_idx:2' in line:
       parts = [p for p in line.split()]
       accuracy_boat = float(parts[3].split(':')[1].strip(','))
       iou_val_boat = float(parts[4].split(':')[1].strip(','))
       acc_boat = np.append(acc_boat,accuracy_boat)
       iou_boat = np.append(iou_boat,iou_val_boat)
'''
   elif 'class_idx:1' in line:
       parts = [p for p in line.split()]
       accuracy_bckg = float(parts[3].split(':')[1].strip(','))
       iou_val_bckg = float(parts[4].split(':')[1].strip(','))
       acc_bckg = np.append(acc_bckg,accuracy_bckg)
       iou_bckg = np.append(iou_bckg,iou_val_bckg) 
'''
plt.figure()
big_file.close()
plt.plot(acc_boat)
plt.title('acc_boat')
plt.show()
plt.figure()
plt.plot(iou_boat)
plt.title('iou_boat')
'''
plt.figure()
big_file.close()
plt.plot(acc_bckg)
plt.title('acc_bckg')
plt.show()
plt.figure()
plt.plot(iou_bckg)
plt.title('iou_bckg')
'''