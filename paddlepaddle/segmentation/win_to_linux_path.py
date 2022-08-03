import os

if __name__ == '__main__':
    base_path = 'C:\\Users\\hp\\Desktop'
    save_path = 'C:\\Users\\hp\\Desktop'
    
    file_name = ['train.txt', 'val.txt', 'test.txt']
    dst_file_name = ['train_list.txt', 'val_list.txt', 'test_list.txt']
    
    retain_source_file = False
    
for file, dst_file in zip(file_name, dst_file_name):
    
    temp_list = []
    with open(os.path.join(base_path, file), 'r+') as f, open(os.path.join(base_path, dst_file), 'w') as f2:
        text = f.readline()
        while text:
            temp_list = text.split('\\')
            f2.write(temp_list[0]+'/'+temp_list[1]+'/'+temp_list[2])
            
            text = f.readline()


    if retain_source_file == False:
        os.remove(os.path.join(base_path, file))