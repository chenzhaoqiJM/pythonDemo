# %%
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
from PIL import Image
import os

# %%
src_mask_path = r"F:\data1\gtFine"
target_mask_path = r"F:\data1\gtFine2"

# %%
def get_color_map_list(num_classes):
    """
    Returns the color map for visualizing the segmentation mask,
    which can support arbitrary number of classes.
    Args:
        num_classes (int): Number of classes.
    Returns:
        (list). The color map.
    """

    num_classes += 1
    color_map = num_classes * [0, 0, 0]
    for i in range(0, num_classes):
        j = 0
        lab = i
        while lab:
            color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
            color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
            color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
            j += 1
            lab >>= 3
    color_map = color_map[3:]
    return color_map

# %%
color_map = get_color_map_list(256)

# %%
imgs_name = []
for _item in os.listdir(src_mask_path):
    if _item.split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg']:
        imgs_name.append(_item)

# %%
spa_num = len(imgs_name)
for i in range(0, len(imgs_name)):
    img_mask = Image.open(os.path.join(src_mask_path, imgs_name[i]))
    img_mask = np.array(img_mask)
   
    # 保存新图片和标签
    _new_img_name = imgs_name[i].split('.')[0] + '.png'
    new_img_mask = img_mask
    lbl_pil = Image.fromarray(new_img_mask.astype(np.uint8), mode='P')
    lbl_pil.putpalette(color_map)
    lbl_pil.save(os.path.join(target_mask_path, _new_img_name))
    print('\r当前进度: {0}{1}%'.format('▉'*(i//spa_num),((i*10)//spa_num)), end='')
print('转换完成！')



