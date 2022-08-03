from inspect import _void
import numpy as np
import cv2
import time
import os
from cContoursAnalyze import ContoursAnalyze, AuxiliaryMeans


#测试文件夹
# test_dir = 'C:\\Users\\hp\\Desktop\\gj\\back_light\\1\\'
test_dir = 'E:\\temp\\gj\\back_light\\3\\'

files_name = os.listdir(test_dir)
imgs_name = [] #只取.bmp文件
for name in files_name:
    if name.split('.')[-1] == 'bmp':
        imgs_name.append(name)


#初始化参数
threshold1 = 50 #canny边缘检测阈值
threshold2 = 200
b1 = 120 #二值化阈值
index_tune= 0 #轮廓的初始索引
index_img = 0 #图片的初始索引

#滑动条回调函数
def void(t):
    pass

cv2.namedWindow('source',0);cv2.namedWindow('contours',0);cv2.namedWindow('binary',0);cv2.namedWindow('canny',0);
cv2.createTrackbar('cannyThre1', 'canny', threshold1, 200, void)
cv2.createTrackbar('cannyThre2', 'canny', threshold2, 400, void)
cv2.createTrackbar('binaryTh', 'binary', b1, 244, void)

analyzer = ContoursAnalyze()
tools = AuxiliaryMeans()

#设置模板
imgtep = cv2.imread(os.path.join(test_dir, "10_true.bmp"), 1)
# imgtep = cv2.imread(os.path.join(test_dir, "Camcap_20220117_165921.bmp"), 1)

analyzer.initTemplate(imgtep)

while True:
    imgpath = os.path.join(test_dir, imgs_name[index_img])
    img = cv2.imread(imgpath, 1)
    img_copy = img.copy() #复制原图片
    imgtep_copy = imgtep.copy()
    
    t0 = time.time()
    contoursFeatures = analyzer.fg(img, threshold1, threshold2, b1, index_tune)
    
    contours, idx, poly, hull, minRect = contoursFeatures["contours"], contoursFeatures["contourIndex"]\
        ,contoursFeatures["poly"],contoursFeatures["hull"],contoursFeatures["minRect"]
    rcontour = analyzer.rotateContours(contoursFeatures)
    
    #获取最小包围圆
    minCircle = cv2.minEnclosingCircle(poly)
    print('最小包围圆', minCircle)
    cv2.circle(img_copy, [int(minCircle[0][0]), int(minCircle[0][1])], int(minCircle[1]), (255,122,150),thickness=12)

    b1 = cv2.getTrackbarPos('binaryTh', 'binary')
    threshold1 = cv2.getTrackbarPos('cannyThre1', 'canny')
    threshold2 = cv2.getTrackbarPos('cannyThre2', 'canny')

    print("矩形框:", contoursFeatures["minRect"])
    # print('原轮廓的点数',contours[idx].shape)
    # print('多边形的点数',poly[0].shape)
    # print("外接多边形的宽高:",(minRect[1][0], minRect[1][1]))
    # print("模板轮廓外接多边形的宽高:",(analyzer.template1["minRect"][1][0], analyzer.template1["minRect"][1][1]))
    
    comScore =  analyzer.contoursCompare(contoursFeatures) #不旋转轮廓，直接比对
    comRScore = analyzer.rotateContoursCompare(contoursFeatures) #旋转轮廓的外接矩形到水平位置再做比较
    
    # lineRes = analyzer.lineComparsion(img_copy,imgtep_copy, contoursFeatures) #逐行比较
    print('total time cost = ', time.time()-t0,'\n')

    #绘图
    analyzer.drawContourFeatures(img_copy, contoursFeatures, 
                                 drawCont=True, drawPoly=False, drawHull=False,drawRect=False)
    analyzer.drawContourFeatures(img_copy, analyzer.rotateContoursFeatures(contoursFeatures), 
                                drawCont=True, drawPoly=False, drawHull=False,drawRect=True)
    
    #画模板的轮廓、外接矩形
    analyzer.drawTemplate(imgtep_copy, tools)

    #书写结果
    sizes = (2048, 2592)
    cv2.putText(img_copy, "Threshold: 0.15", (1800, 200), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0), 17)
    cv2.putText(img_copy, "score: "+str(comRScore)[0:4], (1800, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0), 17)
    if comRScore<0.15:
        cv2.putText(img_copy, "result: YES", (1800, 400), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 17)
    else:
        cv2.putText(img_copy, "result: NO", (1800, 400), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 17)
        
    # cv2.putText(img_copy, 
    # "template:{}, fact:{}, diff:{}".format(str(lineRes[1])[:4], str(lineRes[0])[:4], str(lineRes[0]-lineRes[1])[:5])
    #             , (1400, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 10)

    cv2.imshow('source', img)
    cv2.imshow('contours', img_copy)
          
    cv2.namedWindow('contourstTemplate',0)
    cv2.imshow('contourstTemplate', imgtep_copy)
    cv2.namedWindow('Template',0)
    cv2.imshow('Template', imgtep)
    # cv2.imshow('binary', img_binary)
    # cv2.imshow('canny',img2)
    key = cv2.waitKey(100)
    
    if key == ord('t'):
        index_tune+=1
        if len(contours)-1 < index_tune:
            index_tune = len(contours)-1; print('已经是最后一个轮廓了')
    if key == ord('n'):
        index_img+=1
        if len(imgs_name)-1 < index_img:
            index_img = len(imgs_name)-1
    if key == ord('i'):
        analyzer.step_i+=1

        
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()