import cv2
import numpy as np

img=cv2.imread('C:\\Users\\hp\\Desktop\\1.jpg')

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = 3)
        x_op = x
        if x>img.shape[1]-100:
            x_op = x - 100
        if x<50:
            x_op = x+50
        cv2.putText(img, xy, (x_op, y), cv2.FONT_HERSHEY_PLAIN,
                    4.0, (0,0,255), thickness = 2)
        cv2.imshow("image", img)
cv2.namedWindow("image",0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(0)&0xFF==27:
        break
cv2.destroyAllWindows()