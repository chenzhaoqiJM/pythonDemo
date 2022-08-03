import time
import cv2  



def GetPicture():
    """
    拍照保存图像
    :return:
    """
    # 创建一个窗口
    cv2.namedWindow('camera', 0)
    # 调用摄像头   IP摄像头APP
    # video = "https://192.168.1.141:8080/video"
    video = "http://admin:admin@192.168.1.141:8081/video"
    cap = cv2.VideoCapture(video)
    while True:
        success, img = cap.read()
        cv2.imshow("camera", img)
        # 按键处理
        key = cv2.waitKey(10)
        if key == 27:
            # esc
            break
        if key == 32:
            # 空格
            fileaname = 'frames.jpg'
            cv2.imwrite(fileaname, img)

    # 释放摄像头
    cap.release()
    # 关闭窗口
    cv2.destroyWindow("camera")
    
GetPicture()
