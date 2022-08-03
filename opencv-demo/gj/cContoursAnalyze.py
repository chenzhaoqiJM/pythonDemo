from enum import unique
from inspect import _void
from matplotlib.pyplot import contour
import numpy as np
import cv2
import time
import os

class AuxiliaryMeans():
    def __init__(self):
        pass
    #画斜矩形
    def drawRotateRect(self, img, rotateRect):
        cv2.circle(img, (int(rotateRect[0][0]), int(rotateRect[0][1])), 10, (0,0,255),thickness=10)
        center = np.array([rotateRect[0][0], rotateRect[0][1]]) #矩形的中心，也为平移向量
        w = rotateRect[1][0]; h = rotateRect[1][1]
        pt1 = np.array([0-w/2., 0-h/2.0]); pt2 = np.array([0+w/2.0, 0-h/2.0]) #点以左上角为起点，顺时针取
        pt3 = np.array([0+w/2.0, 0+h/2.0]); pt4 = np.array([0-w/2.0, 0+h/2.0])
        theta = rotateRect[2]/180.0 * np.math.pi
        # M = np.array([[np.math.cos(theta),-np.math.sin(theta)],[np.math.sin(theta), np.math.cos(theta)]]) #旋转矩阵,列向量
        M = np.array([[np.math.cos(theta),-np.math.sin(theta)],[np.math.sin(theta), np.math.cos(theta)]]) #旋转矩阵,列向量
        M = M.T
        pts = [pt1@M+center, pt2@M+center, pt3@M+center, pt4@M+center]
        pts = [[int(item[0]), int(item[1])] for item in pts]
        for i in range(0,4):
            cv2.line(img, pts[i], pts[(i+1)%4], (0,122,255), thickness=12)

class ContoursAnalyze():
    def __init__(self):
        self.template1 = 0
        self.step_i = 1#逐行比较的步长增大倍数
        self.tools = AuxiliaryMeans()
        pass
        
    def fg(self, img,threshold1,threshold2,b1, index_tune):
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰度化
        t0 = time.time()
        # print(b1)
        # b1 = cv2.getTrackbarPos('binaryTh', 'binary')
        retval, img_binary = cv2.threshold(img1, b1, 255, cv2.THRESH_BINARY) #

        # img2 = cv2.Canny(img_binary, threshold1, threshold2,apertureSize=3, L2gradient=True)
        # img2 = cv2.Canny(img1, threshold1, threshold2, apertureSize=3, L2gradient=True)
        # img2 = cv2.Sobel(img1,-1, 1,0,ksize=3 ) + cv2.Sobel(img1,-1, 0,1,ksize=3 )
        # img2 = cv2.Sobel(img_binary,-1, 1,0,ksize=5 ) + cv2.Sobel(img_binary,-1, 0,1,ksize=5 )
        img2 = cv2.Laplacian(img_binary, -1)
        
        #找轮廓并发现最大轮廓
        contours, hierarchy	= cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # contours, hierarchy	= cv2.findContours(img2, cv2.RETR_FLOODFILL, cv2.CHAIN_APPROX_NONE)
        contours = np.array(contours, dtype=object) #轮廓的长度不一样，无法表示为一个固定大小的numpy数组
        contours_size = np.array([len(s) for s in contours ])
        sort_index = np.argsort(-contours_size) #返回从大到小的索引,降序排列
        idx = sort_index[index_tune] #取一个轮廓，按t增加索引

        poly = cv2.approxPolyDP(contours[idx], 2, True) #多边形拟合
        hull = cv2.convexHull(contours[idx]) #轮廓凸包
        
        minRect = cv2.minAreaRect(contours[idx]) #轮廓最小包围矩形, ((x,y),(w,h), angle)
        temp = {"contours":contours, "contourIndex":idx,"poly":poly, "hull":hull, "minRect":minRect}
        
        return  temp
    
    #初始化模板
    def initTemplate(self, img):
        threshold1 = 50 #canny边缘检测阈值
        threshold2 = 200
        b1 = 120 #二值化阈值
        index_tune= 1 #轮廓的初始索引
        self.template1  = self.fg(img, threshold1, threshold2, b1, index_tune)

    
    #直接比较两个轮廓的形状，主要是利用矩
    def contoursCompare(self, contoursFeatures):
        #输入待比较的轮廓特征，确保已经设置好了模板
        if self.template1 == 0:
            print('没有设置模板!!!')
            return
        idx = contoursFeatures["contourIndex"]; tidx = self.template1["contourIndex"]
        t1 = time.time()
        score = cv2.matchShapes(contoursFeatures["contours"][idx], self.template1["contours"][tidx] 
                                ,cv2.CONTOURS_MATCH_I2, 0)
        # retval	=	cv2.createShapeContextDistanceExtractor()
        # score = retval.computeDistance(contoursFeatures["contours"][idx], self.template1["contours"][tidx] )
        t2 = time.time() - t1
        # score_poly = cv2.matchShapes(contoursFeatures["poly"][0], self.template1["poly"][0] ,
        #                              cv2.CONTOURS_MATCH_I2, 0)
        # t3 = time.time() - t2
        # print("直接比较轮廓的结果:{} ,耗费时间为: {}".format(score, t2))
        # print("比较轮廓拟合多边形的效果:{}, 耗费时间为: {}".format(score_poly, t3))
        return score

    #比较两个旋转轮廓的形状，主要是利用矩
    def rotateContoursCompare(self, contoursFeatures):
        #输入待比较的轮廓特征，确保已经设置好了模板
        if self.template1 == 0:
            print('没有设置模板!!!')
            return
        idx = contoursFeatures["contourIndex"]; tidx = self.template1["contourIndex"]
        t1 = time.time()
        score = cv2.matchShapes(self.rotateContours(contoursFeatures), self.rotateContours(self.template1)
                                ,cv2.CONTOURS_MATCH_I2, 0)
        t2 = time.time() - t1
        print("旋转轮廓后直接对比结果:{} ,耗费时间为: {}".format(score, t2))
        return score
    
    def lineComparsion(self, img, imgTmp, contoursFeatures):
        idx = contoursFeatures["contourIndex"]; tidx = self.template1["contourIndex"]
        #得到旋转后的轮廓，数据类型（N,1,2)N为轮廓点数
        rContour, rContourTemp = self.rotateContours(contoursFeatures), self.rotateContours(self.template1)
        rPoly = cv2.approxPolyDP(rContour, 1, True) #多边形拟合
        rPolyTemp = cv2.approxPolyDP(rContourTemp, 1, True) #多边形拟合
        rminRect = cv2.minAreaRect(rContour) #轮廓最小包围矩形
        rminRectTemp = cv2.minAreaRect(rContourTemp) #轮廓最小包围矩形
        #以y轴为基准扫描还是以x轴
        
        #以y为扫描的正方向
        # rContourP_y = rContour[:,0,1] #取y轴元素
        rContourP_y = rPoly[:,0,1] #取y轴元素
        #查找顶部元素所在位置
        topPoint_y = np.min(rContourP_y)
        topPoint = rContour[np.argwhere(rContourP_y==topPoint_y).reshape(-1)[0]][0] #[[x,y]],取里面的一层
        
        bottomPoint_y = np.max(rContourP_y)
        bottomPoint = rContour[np.argwhere(rContourP_y==bottomPoint_y).reshape(-1)[0]][0] #[[x,y]],取里面的一层

        pixelStep = 5
        # temp_y = topPoint_y + pixelStep*self.step_i
        # if temp_y>=bottomPoint_y:
        #     temp_y = bottomPoint_y
        # print(np.argwhere(rContourP_y==temp_y))

        #通过求交线的方式找到点
        p0, p1 = self.findIntersectionfilter(rminRect, pixelStep, rPoly)
        cv2.line(img, ( int(p0[0]),int(p0[1]) ), ( int(p1[0]),int(p1[1]) ), (0,0,255), 12)
        
        rp0, rp1 = self.findIntersectionfilter(rminRectTemp, pixelStep, rPolyTemp) #模板行
        cv2.line(imgTmp, ( int(rp0[0]),int(rp0[1]) ), ( int(rp1[0]),int(rp1[1]) ), (0,0,255), 12)
        return np.array([p1[0]-p0[0], rp1[0]-rp0[0]])
    
    def findIntersection(self, startP, endP, contour, isY = True):
        #点格式要求为[x,y]
        spoint = []
        step = 1; iterTimes = (endP[0]-startP[0])/step
        for i in range(0, int(iterTimes)):
            x = startP[0]+i*step
            retval = cv2.pointPolygonTest(contour, (x, startP[1]), measureDist=True)
            if retval <= 1 and retval>0:
                spoint.append([x, startP[1]])
        spoint = np.array(spoint)
        return spoint
    def findIntersectionfilter(self, minRect, pixelStep, Poly):
        center = np.array([minRect[0][0], minRect[0][1]]) #矩形的中心
        w = minRect[1][0]; h = minRect[1][1]
        leftStart = [center[0]-w/2.0, center[1]-h/2.0]
        rightEnd = [center[0]+w/2.0, center[1]+h/2.0]    
        startP = leftStart; startP[1]+=pixelStep*self.step_i
        endP = rightEnd; endP[1]+=pixelStep*self.step_i
        res = self.findIntersection(startP, endP, Poly)
        sortIndex = np.argsort(res[:,0]) #升序排列
        p0 = res[sortIndex[0]]; p1 = res[sortIndex[-1]]
        return np.array([p0, p1])

      
    #旋转轮廓到水平位置
    def rotateContours(self,contoursFeatures):
        rotateRect = contoursFeatures["minRect"]
        idx = contoursFeatures["contourIndex"]
        center = np.array([rotateRect[0][0], rotateRect[0][1]]) #矩形的中心，也为平移向量
        w = rotateRect[1][0]; h = rotateRect[1][1]
        theta = rotateRect[2]
        if theta>70:
            theta = theta - 90.0
        theta = theta/180.0 * np.math.pi
        #旋转矩阵,列向量
        M = np.array([[np.math.cos(theta),-np.math.sin(theta)],[np.math.sin(theta), np.math.cos(theta)]]) 
        M_Inv = np.linalg.inv(M)
        M = M_Inv.T #行向量形式
        
        t1 = time.time()
        contour = (contoursFeatures["contours"][idx] - center)@M + center #旋转轮廓点,先移动到零点，再还原
        contour = contour.astype(np.int32) #必须转换成整数以满足opencv对像素点的定义
        t1 = time.time() - t1
        # print(rotateRect[2])
        return contour
    def rotateContoursFeatures(self,contoursFeatures):
        contour = np.array([self.rotateContours(contoursFeatures)])
        poly = cv2.approxPolyDP(contour[0], 2, True) #多边形拟合
        hull = cv2.convexHull(contour[0]) #轮廓凸包
        minRect = cv2.minAreaRect(contour[0]) #轮廓最小包围矩形
        temp = {"contours":contour, "contourIndex":0,"poly":poly, "hull":hull, "minRect":minRect}
        return  temp
    
    
#绘图
    #画模板
    def drawTemplate(self, img, tools):
        self.drawContourFeatures(img, self.template1, 
                                 drawCont=True, drawPoly=False, drawHull=False,drawRect=False)
        self.drawContourFeatures(img, self.rotateContoursFeatures(self.template1), 
                                 drawCont=True, drawPoly=False, drawHull=False,drawRect=True)

    #画轮廓等特征
    def drawContourFeatures(self, img,contoursFeatures, drawCont=True, drawPoly=True, drawHull=True, drawRect=True):
        if drawCont:
            contours, idx = contoursFeatures["contours"],contoursFeatures["contourIndex"]
            cv2.drawContours(img, contours, idx, (0,255,0), thickness=12) #画原轮廓，绿色
        if drawPoly:
            cv2.drawContours(img, [contoursFeatures["poly"]], 0, (0,0,255), thickness=12) #画多边形，红色的
        if drawHull:
            cv2.drawContours(img, [contoursFeatures["hull"]], 0, (255,100,78), thickness=7) #画轮廓凸包
        if drawRect:
            self.tools.drawRotateRect(img, contoursFeatures["minRect"]) #画轮廓凸包
            

    