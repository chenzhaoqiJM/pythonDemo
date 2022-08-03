from inspect import _void
from turtle import mode
import numpy as np
import cv2
import time
import os
from cContoursAnalyze import ContoursAnalyze, AuxiliaryMeans
from sklearn.svm import SVC # "Support vector classifier"



#测试文件夹
# test_dir = 'C:\\Users\\hp\\Desktop\\gj\\back_light\\1\\'
test_dir = 'C:\\Users\\hp\\Desktop\\gj\\back_light\\2\\'

files_name = os.listdir(test_dir)
imgs_name = [] #只取.bmp文件
for name in files_name:
    if name.split('.')[-1] == 'bmp':
        imgs_name.append(name)


#初始化参数
threshold1 = 50 #canny边缘检测阈值
threshold2 = 200
b1 = 120 #二值化阈值
index_tune= 1 #轮廓的初始索引
index_img = 0 #图片的初始索引


analyzer = ContoursAnalyze()
tools = AuxiliaryMeans()

#设置模板
imgtep = cv2.imread(os.path.join(test_dir, "10_true.bmp"), 1)
analyzer.initTemplate(imgtep)


train_file_list = imgs_name[0:7]
test_file_list = imgs_name[7:]


def get_features(file_list):
    X = []; y=[]
    for imgName in file_list:
        imgpath = os.path.join(test_dir, imgName)
        img = cv2.imread(imgpath, 1)
        contoursFeatures = analyzer.fg(img, threshold1, threshold2, b1, index_tune)
        contours, idx, poly, hull, minRect = contoursFeatures["contours"], contoursFeatures["contourIndex"]\
        ,contoursFeatures["poly"],contoursFeatures["hull"],contoursFeatures["minRect"]
        
        arc = cv2.arcLength(contours[idx], True) #轮廓周长
        minCircle = cv2.minEnclosingCircle(poly) #最小包围圆（（x,y), radius)
        comScore =  analyzer.contoursCompare(contoursFeatures) #不旋转轮廓，直接比对，返回float类型分数

        feature = [arc, comScore, minCircle[0][0], minCircle[0][1], minCircle[1], 
                minRect[0][0],minRect[0][1], minRect[1][0], minRect[1][1], minRect[2]]
        X.append(feature)
        
        tag = imgName.split('.')[0]
        tag = tag.split('_')[-1]
        if tag == 'false':
            y.append(0)
        else:
            y.append(1)
            
    return np.array(X), np.array(y)

X, y = get_features(train_file_list)

print(X.shape)
print(y.shape)

model = SVC(kernel='linear', C=1E10) #支撑向量机，线性内核
model.fit(X, y)

#训练集测试
y_pred = model.predict(X)
print(y)
print(y_pred)

#测试集
print('验证集测试')
X_test, y_test = get_features(test_file_list)
print(X_test.shape)
y_test_pre = model.predict(X_test)
print(y_test)
print(y_test_pre)