import numpy as np
import cv2

img = cv2.imread('E:\\Comm\\demo\\2.jpg', 1)

img1 = cv2.GaussianBlur(img, (5,5), 0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.Laplacian(img2, 0)
img4 = img2 + img3

imgShape = (np.shape(img)[0], np.shape(img)[1], 1)
img_eHist0 = cv2.equalizeHist(img[:,:,0]) 
img_eHist1 = cv2.equalizeHist(img[:,:,1]) 
img_eHist2 = cv2.equalizeHist(img[:,:,2]) 

img_eHist = np.concatenate([np.reshape(img_eHist0,imgShape), \
    np.reshape(img_eHist1,imgShape), np.reshape(img_eHist2,imgShape)], axis=2)

img6 = img.astype(np.float32)/255.0 * 1.5


white_noise = np.random.standard_normal(img.shape)
img7 = img.astype(np.float32)/255.0
img7 = img7 + white_noise/10

img7 = (img7 / np.max(img7.reshape(-1)))
# img7 = cv2.randn(img7, 1, 1)

cv2.imwrite('C:\\Users\\hp\\Desktop\\10.jpg', img7)
cv2.imshow('zq', img7)
cv2.waitKey()