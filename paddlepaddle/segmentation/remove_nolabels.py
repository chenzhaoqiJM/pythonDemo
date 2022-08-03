import os

if __name__ == '__main__':
    path = 'C:\\Users\\hp\\PaddleSeg\\dataset\\leimu\\JPEGImages'
    
    file_list = os.listdir(path)
    
    count = 0
    print('一共{}个元素'.format(len(file_list)))
    for file_item in file_list:
        if len(file_item)>=4 and file_item[-3:] == 'jpg':
            json_file_name = file_item.split('.')[0]+'.json'

            if json_file_name not in file_list:
                os.remove(os.path.join(path, file_item))
                count += 1
                print('删除了{}个'.format(count))
    # print(file_list)