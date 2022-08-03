import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


def draw_axix(img):
    width = img.shape[0]
    height = img.shape[1]
    offset = 20
    step = 100
    cv2.arrowedLine(img, (offset, height//2), (width-offset, height//2), (0,0,0), 1,8,0, 0.01)
    cv2.arrowedLine(img, (width//2, height-offset), (width//2, offset), (0,0,0), 1,8,0, 0.01)
    for i in range(0, step, 2):
        of1 = i * 2 * pixel_to_axis //step
        of2 = of1 + 2*pixel_to_axis//step
        #水平虚线
        cv2.line(img, (width//2-pixel_to_axis + of1, height//2-pixel_to_axis), (width//2-pixel_to_axis+of2, height//2-pixel_to_axis)\
            ,(255, 0, 0), 2, lineType= cv2.FILLED)
        cv2.line(img, (width//2-pixel_to_axis + of1, height//2+pixel_to_axis), (width//2-pixel_to_axis+of2, height//2+pixel_to_axis)\
            ,(255, 0, 0), 2, lineType= cv2.FILLED)
        #垂直虚线
        cv2.line(img, (width//2-pixel_to_axis , height//2-pixel_to_axis+of1), (width//2-pixel_to_axis, height//2-pixel_to_axis+of2)\
            ,(255, 0, 0), 2, lineType= cv2.FILLED)
        cv2.line(img, (width//2+pixel_to_axis , height//2-pixel_to_axis+of1), (width//2+pixel_to_axis, height//2-pixel_to_axis+of2)\
            ,(255, 0, 0), 2, lineType= cv2.FILLED)
        
def draw_point_and_vector(img, xk):
    width = img.shape[0]
    height = img.shape[1]
    center = (width//2, height//2)
    pt = (width//2 + int(xk[0][0]*pixel_to_axis), height//2- int(xk[1][0]*pixel_to_axis))
    cv2.circle(img, pt, 8, (0, 255,0), 8)
    pfar = (width//2 + int(xk[0][0]*pixel_to_axis * 1000), height//2 - int(xk[1][0]*pixel_to_axis*1000))
    cv2.line(img, center, pfar, (0,0,255), 2)
    
        
    
if __name__ == '__main__':
    
    A = [[13.0,18.0] ,[3.0,77.0]]
    x0 = [[-1.0], [1.0]]
    xk = x0
    uk = 0
    
    delay_time = 200
    iter_times = 100
    bit_size = 25
    
    A = np.array(A, dtype=np.float64)
    x0 = np.array(x0, dtype=np.float64)
    
    img = np.zeros((800,800,3) ,np.uint8)
    img[:,:] = [255,255,255]
    pixel_to_axis = img.shape[0]//5
    
    
    cv2.namedWindow('main',1)
    draw_axix(img)
    cv2.imshow('main',img)
    
    cv2.waitKey(1000)
    draw_point_and_vector(img, xk)
    cv2.imshow('main', img)
    cv2.waitKey(2000)
     
    
    vector_val_list = []
    for i in range(0, iter_times):
        xk = A.dot(xk)
        vector_val_list = [item[0] for item in xk]
        uk = max(vector_val_list)
        print('xk:{}  uk:{}  xk+1:{}'.format(xk.reshape(-1), uk, (xk/uk).reshape(-1) ))
        print('\n')
        xk = xk/uk
        
        img[:,:] = [255,255,255]
        draw_axix(img)
        draw_point_and_vector(img, xk)
        cv2.putText(img, 'The '+str(i+1)+' second iter', (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,122, 122), 3)
        cv2.putText(img, '[{}, {}]'.format(str(xk[0][0])[:bit_size], str(xk[1][0])[:bit_size]), \
            (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (222,122, 122), 3)
        cv2.putText(img, 'uk = {}'.format(str(uk)[:bit_size]), (40, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (222,122, 122), 3)
        cv2.imshow('main',img)
        cv2.waitKey(delay_time)
        
    cv2.waitKey()
    print(xk)
    print(uk)