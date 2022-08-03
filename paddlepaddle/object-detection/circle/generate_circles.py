import cv2
import numpy as np

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    images_width = np.random.randint(400, 650, size=2000)
    images_height = np.random.randint(400, 600, size=2000)
    
    image = np.ndarray((images_width[0], images_height[0],3), dtype=np.uint8, buffer=np.array([122,122,122]))
    
    cv2.imshow('1', image)
    cv2.waitKey()
    print(images_width)