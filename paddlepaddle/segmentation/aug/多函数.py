import numpy as np



def full_the_roi(img, full_content, roi, mix_step = 2):
    # 一小块背景填充一个大区域
    # img rgb array
    img = np.array(img)
    # img[roi[0]:roi[1], roi[2]:roi[3], :] = full_content# 给指定区域指定颜色
    
    _h = full_content.shape[0]
    _w = full_content.shape[1]
    _rows = (roi[1]-roi[0])//_h
    _cols = (roi[3]-roi[2])//_w
    for i in range(0, _rows+1): #多填充一块
        for j in range(0, _cols+0):
            if i==0:
                if j == 0: 
                    img[roi[0]+_h*i:roi[0]+_h*(i+1), roi[2]+_w*j:roi[2]+_w*(j+1)] = full_content
                else:
                    img[roi[0]+_h*i:roi[0]+_h*(i+1), roi[2]+_w*j-mix_step:roi[2]+_w*(j+1)-mix_step] = full_content
            else:
                if j == 0: 
                    img[roi[0]+_h*i-mix_step:roi[0]+_h*(i+1)-mix_step, roi[2]+_w*j:roi[2]+_w*(j+1)] = full_content
                else:
                    img[roi[0]+_h*i-mix_step:roi[0]+_h*(i+1)-mix_step, roi[2]+_w*j-mix_step:roi[2]+_w*(j+1)-mix_step] = full_content
    return img