from inspect import _void
import numpy as np
import cv2
import time
import os

test_dir = 'C:\\Users\\hp\\Desktop\\gj\\circle_light\\3\\'
img = cv2.imread(os.path.join(test_dir, "Camcap_20220117_162708.bmp"), 1)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_copy = img.copy()

retval, img_binary = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) #
img_erod = cv2.erode(img_binary, cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))


mask = np.zeros([img.shape[0]+2, img.shape[1]+2], dtype=np.uint8) #不填充掩膜里面的非零区域

retval, image, mask, rect	 = cv2.floodFill(img_copy, mask, (1105, 1839), 0, loDiff=(12,12,12), upDiff=(9,9,9))
cv2.namedWindow('source',0)
cv2.namedWindow('b',0)
cv2.imshow('source', img)
cv2.imshow('b', image)
cv2.waitKey()