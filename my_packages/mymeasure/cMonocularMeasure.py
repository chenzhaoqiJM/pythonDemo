import numpy as np
import cv2

class MonocularMeasure():
    def __init__(self):
        self.pnp = 0.0
        
    def findHByCalibrationPlate(self,singleImgPath = 'C:\\Users\\hp\\Desktop\\0.jpg' ,
                                chessSize=[7,7], chessCellLen = 5.0, mode = 'circle'):
        """对一张图片,图片中一张标定板，求像素平面到标定板平面的单应性矩阵
        >>> 形参:singleImgPath-图片所在的绝对路径,例:'C:\\Users\\hp\\Desktop\\0.jpg'
        >>> 形参:chessSize-标定板上点的行数、列数，chessCellLen-标定板上两个点之间的实际距离,单位mm
        >>> 形参:mode-标定板的样式，可选'circle'或者'square'
        >>> 返回值: 单应性矩阵H, 从像素坐标到实际坐标的映射。(要求实际坐标到像素坐标则对该矩阵取逆)
        """
        src_left = singleImgPath
        _monocular_chessSize = chessSize
        _monocular_chessCellLen =  chessCellLen #mm

        objp = np.zeros((_monocular_chessSize[0]*_monocular_chessSize[1], 3), np.float32)
        for i in range(0, _monocular_chessSize[1]):#row
            for j in range(0, _monocular_chessSize[0]): #col
                point = [j*_monocular_chessCellLen, i*_monocular_chessCellLen, 0.]
                objp[i*_monocular_chessSize[0]+j][0] = point[0]
                objp[i*_monocular_chessSize[0]+j][1] = point[1]
                objp[i*_monocular_chessSize[0]+j][2] = point[2]
        apoints = objp
        # termination criteria， 迭代的终止条件
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        col = _monocular_chessSize[0]; row = _monocular_chessSize[1]

        if mode == 'square':
            ret_l, corners_left = cv2.findChessboardCorners(src_left, (col,row), None)
        if mode == 'circle':
            flags = cv2.CALIB_CB_SYMMETRIC_GRID
            ret_l, corners_left = cv2.findCirclesGrid(src_left, (col,row), flags)
        if(ret_l == True ):
            print('check!!!!!!!!!')
            pass

        corners_left = corners_left.reshape(col*row,2)
        h, mask = cv2.findHomography( corners_left, apoints[:,:-1],method=cv2.RANSAC)
        return h
        
    def findCornersAndWorldPoints(self,singleImgPath = 'C:\\Users\\hp\\Desktop\\0.jpg' ,
                                  chessSize=[7,7], chessCellLen = 5.0, mode = 'circle'):
        """对一张图片,求一张标定板上对应点的像素坐标及这些点在标定板平面上的实际坐标(实际坐标默认Z=0)。
        >>> 形参:singleImgPath-图片所在的绝对路径,例:'C:\\Users\\hp\\Desktop\\0.jpg'
        >>> 形参:chessSize-标定板上点的行数、列数，chessCellLen-标定板上两个点之间的实际距离,单位mm
        >>> 形参:mode-标定板的样式，可选'circle'或者'square'
        >>> 返回值: 是否在图像中检测到标定板并成功提取点, 标点板点实际坐标, 标定板点像素坐标
        """
        src_left = cv2.imread(singleImgPath, 0)
        _monocular_chessSize = chessSize
        _monocular_chessCellLen =  chessCellLen #mm

        objp = np.zeros((_monocular_chessSize[0]*_monocular_chessSize[1], 3), np.float32)
        for i in range(0, _monocular_chessSize[1]):#row
            for j in range(0, _monocular_chessSize[0]): #col
                point = [j*_monocular_chessCellLen, i*_monocular_chessCellLen, 0.]
                objp[i*_monocular_chessSize[0]+j][0] = point[0]
                objp[i*_monocular_chessSize[0]+j][1] = point[1]
                objp[i*_monocular_chessSize[0]+j][2] = point[2]
        apoints = objp
        # termination criteria， 迭代的终止条件
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        col = _monocular_chessSize[0]; row = _monocular_chessSize[1]

        if mode == 'square':
            ret_l, corners_left = cv2.findChessboardCorners(src_left, (col,row), None)
        if mode == 'circle':
            flags = cv2.CALIB_CB_SYMMETRIC_GRID
            params = cv2.SimpleBlobDetector_Params()
            # params.maxCircularity = 1000
            params.maxArea = 100000
            blob = cv2.SimpleBlobDetector_create(params)
            pra = cv2.CirclesGridFinderParameters()
            # src_left = cv2.resize(src_left, (src_left.shape[0],src_left.shape[1]))
            ret_l, corners_left = cv2.findCirclesGrid(src_left, (col,row), flags, blob, pra)
        if(ret_l == True ):
            print('check!!!!!!!!!')
            pass
        corners_left = corners_left.reshape(col*row,2)
        return ret_l, apoints, corners_left
    
    def findHByPnPAndZDiff(self, cameraMatrix, distCoeff, worldPoints, pixelPoints, zLow=0):
        """利用外参的旋转矩阵和平移向量、相机内参，测量与标定平面在Z方向相距L处平面上任意两点实际距离。
        >>> 形参:cameraMatrix-相机内参数(固有参数), distCoeff-相机畸变向量(固有参数)
        >>> 形参:worldPoints-标定板上点的实际坐标值，pixelPoints-标定板上点像素坐标值,用findCornersAndWorldPoints函数得到
        >>> 形参:zLow-标定平面相对于被测平面的距离，标定平面为0，以标定平面为基准远离相机取负值
        >>> 返回值: 单应性矩阵H, 从像素坐标到实际坐标的映射。(要求实际坐标到像素坐标则对该矩阵取逆)
        """
        A = cameraMatrix
        distCoeff = distCoeff
        retvel, rvec, tvec = cv2.solvePnP(worldPoints, pixelPoints, cameraMatrix=A,distCoeffs=distCoeff)
        W, jaconbin = cv2.Rodrigues(rvec)
        # print(W,'\n',tvec)
        W0 = W.copy()
        W0[:,2] = tvec.reshape(-1) - zLow*W0[:,2]
        H0 = A @ W0 #从实际坐标到像素坐标
        H0 = np.linalg.inv(H0) #从像素坐标到实际坐标
        H0 = H0 / H0[2][2] #齐次化最后一个参数, 可以不用
        return H0
        
