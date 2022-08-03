import cv2
import numpy as np
import time

class ContoursCommonHelper(object):
    @staticmethod
    def drawRotateRectCV( img, rotateRect, color = (0,122,255), thickness= 5):
        points = cv2.boxPoints(rotateRect)
        for i in range(0,4):
            cv2.line(img, [int(points[i][0]), int(points[i][1])], [int(points[(i+1)%4][0]), int(points[(i+1)%4][1])], 
                     color, thickness=thickness)
            
    @staticmethod
    def find_coutour_corner(poly, deg_th_up = 140, deg_th_down = 40, dis_th = 20):
        # 传入参数：轮廓[ [[]], [[]], [[]], .........]
        # 传出参数：点集 [[], [], [], .........]
        lenpoly = len(poly)
        point_list = []
        t1 = time.time()
        for i in range(0, lenpoly-1):
            p0 = poly[i][0] #当前点 [[]], 取最里面的一层
            pfront = poly[i-1][0]
            pback = poly[(i+1)%lenpoly][0]
            vec1 = pfront - p0
            vec2 = pback - p0
            vec1 = vec1 * 1.0
            vec2 = vec2 * 1.0
            angle = np.math.acos( (np.dot(vec1, vec2))/ np.math.sqrt((np.dot(vec1,vec1)) * (np.dot(vec2, vec2))) )
            degree = np.abs( angle*180/np.math.pi )%180
            if ( degree < deg_th_up and degree > deg_th_down ):
                point_list.append(p0)
        

        # 把重合的点过滤掉
        len_point_list = len(point_list)
        new_point_list = []

        temp = np.array([0,0])
        count_peer = 0
        #多循环一次
        for i in range(0, len_point_list): 
            p0 = point_list[i]
            p1 = point_list[(i+1)%len_point_list]
            v = p0-p1
            distance = np.math.sqrt(np.dot(v, v))
            
            if distance <= dis_th:
                temp = temp + p0
                count_peer = count_peer + 1
            else:
                if count_peer >= 1:
                    temp += p0
                    count_peer += 1
                    new_point_list.append(temp/count_peer)
                    count_peer = 0 
                    temp =  np.array([0,0])
                    continue
                
                new_point_list.append(p0)
        print('耗时为：', time.time()-t1)
        return new_point_list