# %%
import numpy as np
import cv2
from PIL import Image
import os
import xml.dom.minidom

# %%
mask_img_path = r'F:\data1\gtFine'
src_img_path = r'F:\data1\leftImg8bit'
save_path = r'F:\data1\newImg\annotations'


if not os.path.exists(save_path):
    os.makedirs(save_path)
masks_name = []
for _item in os.listdir(mask_img_path):
    if _item.split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg']:
        masks_name.append(_item)
imgs_name = []
for _item in os.listdir(src_img_path):
    if _item.split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg']:
        imgs_name.append(_item)

# %%
def rect_to_xml(base_info, objects, base_keys, bndbox_keys, save_xml_path):
  base_info_dict = base_info
  objectList = objects
  base_keys = base_keys
  bndbox_keys = bndbox_keys
  
  save_xml_name = save_xml_path
  
  #在内存中创建一个空的文档
  doc = xml.dom.minidom.Document() 
  #创建一个根节点Managers对象
  root = doc.createElement('annotation') 
  #将根节点添加到文档对象中
  doc.appendChild(root) 

  folder = doc.createElement('folder')
  folder.appendChild(doc.createTextNode(base_info_dict['folder']))
  root.appendChild(folder)

  filename = doc.createElement('filename')
  filename.appendChild(doc.createTextNode(base_info_dict['filename']))
  root.appendChild(filename)

  path = doc.createElement('path')
  path.appendChild(doc.createTextNode(base_info_dict['path']))
  root.appendChild(path)

  source = doc.createElement('source')
  database = doc.createElement('database')
  database.appendChild(doc.createTextNode(base_info_dict['database']))
  source.appendChild(database)
  root.appendChild(source)

  size = doc.createElement('size')
  width = doc.createElement('width')
  width.appendChild(doc.createTextNode(base_info_dict['width']))
  height = doc.createElement('height')
  height.appendChild(doc.createTextNode(base_info_dict['height']))
  depth = doc.createElement('depth')
  depth.appendChild(doc.createTextNode(base_info_dict['depth']))
  size.appendChild(width); size.appendChild(height); size.appendChild(depth)
  root.appendChild(size)

  segmented = doc.createElement('segmented')
  segmented.appendChild(doc.createTextNode(base_info_dict['segmented']))
  root.appendChild(segmented)

  for box in objectList :
    nodeObject = doc.createElement('object')
    
    for base_key in base_keys:
          subnode = doc.createElement(base_key); subnode.appendChild(doc.createTextNode(str(box[base_key])));
          nodeObject.appendChild(subnode)
    
    bndbox = doc.createElement('bndbox')
    for bndbox_key in bndbox_keys:
      subNode = doc.createElement(bndbox_key); subNode.appendChild(doc.createTextNode(str(box['bndbox'][bndbox_key])))
      bndbox.appendChild(subNode)
    nodeObject.appendChild(bndbox)

    root.appendChild(nodeObject)
    
  #开始写xml文档
  fp = open(save_xml_name, 'w')
  doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
  fp.close()


# %%
def isInRect(rect1, rect2):
    # 判断rect2是否在rect1内
    leftx1, lefty1, rightx1, righty1 = rect1[0], rect1[1], rect1[0]+rect1[2], rect1[1]+rect1[3]
    leftx2, lefty2, rightx2, righty2 = rect2[0], rect2[1], rect2[0]+rect2[2], rect2[1]+rect2[3]
    if (leftx1 == leftx2 and lefty1 == lefty2 ) and (rightx1 == rightx2 and righty1 == righty2):
        return False
    if (leftx1 <= leftx2 and lefty1 <= lefty2 ) and (rightx1 >= rightx2 and righty1 >= righty2):
        return True
    else:
        return False
    
def check_mix(rectList, min_len=2):
    _rectList1 = []
    for _rect in rectList:
        if _rect[2] >= min_len and _rect[3] >= min_len:
            _rectList1.append(_rect)
            
    _rectList1_copy = _rectList1.copy()
  
    for i in range(0, len(_rectList1)):
        _rect1 = _rectList1[i]
        temp_ = []
        for _rect2 in _rectList1_copy:
            _flag = isInRect(_rect1, _rect2)
            if _flag == True:
                temp_.append(_rect2)
        for _waitRe in temp_:
            _rectList1_copy.remove(_waitRe)
        
    return _rectList1_copy

# %%
spa_num = len(masks_name)
for _i, _maskName in enumerate(masks_name):
    _name = _maskName.split('.')[0]
    _find_src = False
    for _fix in ['jpg', 'png', 'bmp', 'jpeg']:
        _src_name = _name + '.' + _fix
        if _src_name in imgs_name:
            _find_src = True
            break
    if _find_src == False:
        continue
    
    img = np.array(Image.open(os.path.join(mask_img_path, _maskName)))
    src_img = np.array(Image.open(os.path.join(src_img_path, _src_name)))
    
    new_img = np.zeros_like(img, dtype=np.uint8)
    new_img[img == 1] = 255

    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
    new_img = cv2.morphologyEx(new_img, cv2.MORPH_CLOSE, se)
    # edge = cv2.Canny(new_img, 200, 300)
    edge = cv2.Laplacian(new_img, -1)
    contours, hierarchy	= cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contours_size = np.array([len(s) for s in contours ])
    sort_index = np.argsort(-contours_size) #返回从大到小的索引,降序排列
    # idx = sort_index[0] #取一个轮廓
    
    rectList1 = []
    for _idx in sort_index:
        rect = cv2.boundingRect(contours[_idx])
        rectList1.append(rect)
    rectList = check_mix(rectList1)
        
    base_info_dict = {'folder':'newImg', 'filename':'1.jpg', 'path':r'F:\data1\newImg\1.jpg', 
                    'database':'Unknown', 'width':'1000', 'height':'800', 'depth':'3', 'segmented':'0'}

    h, w, ddp = src_img.shape
    base_info_dict['folder'] = 'leftImg8bit'; base_info_dict['filename']=_src_name
    base_info_dict['path'] = os.path.join(src_img_path, _src_name)
    base_info_dict['width'] = str(w); base_info_dict['height'] = str(h); base_info_dict['depth'] = str(ddp)

    objectList = []
    for rect in rectList:
        xmin, ymin, xmax, ymax = str(rect[0]), str(rect[1]), str(rect[0]+rect[2]), str(rect[1]+rect[3])
        sub_dict = {'name':'fall', 'pose':'Unspecified', 'truncated':'0', 'difficult':0,
                    'bndbox':{'xmin':xmin, 'ymin':ymin, 'xmax':xmax, 'ymax':ymax}}
        objectList.append(sub_dict)
    base_keys = ['name', 'pose', 'truncated', 'difficult']
    bndbox_keys = ['xmin', 'ymin', 'xmax', 'ymax']

    save_xml_name = os.path.join(save_path, _src_name.split('.')[0]+'.xml')
    
    rect_to_xml(base_info_dict, objectList, base_keys, bndbox_keys, save_xml_name)
   
    print('\r当前进度: {0}{1}%'.format('▉'*(int(float(_i)/float(spa_num)*20)),(int(float(_i)/float(spa_num)*100))), end='')
print('转换完成！')
    # _src = src_img.copy()
    # for _idx in sort_index:
    #     rect = cv2.boundingRect(contours[_idx])
        
    #     cv2.drawContours(_src, contours, _idx, (0,255,0), thickness=3) #画原轮廓，绿色
    #     cv2.rectangle(_src, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), color=(255, 0, 0), thickness=5)
    
    # _src = cv2.cvtColor(_src, cv2.COLOR_RGB2BGR)  
    # cv2.imwrite(os.path.join(save_path, str(_i+1)+'.jpg'), _src)
    

# %%



