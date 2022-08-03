import requests
import os
from clint.textui import progress


class SingleFileDownloads():
    def __init__(self):
        self.single_img_url_ = ''
        
    def download_single_img(self, url, headers, save_path = './', file_name = ''):
        if file_name == '':
            s = url.split('.')
            file_name = s[-2][-10:-1]+'.'+s[-1]
            
        
        if(file_name.find('.') == -1): #如果提供的文件名没有后缀名就加上一个后缀
            suffix_name = self.img_suffix_check(url) #提取后缀名
            file_name = file_name + suffix_name
        
        full_path = os.path.join(save_path, file_name) #拼接完整的路径
        # print(full_path)
        try:
            if not os.path.exists(save_path): #保存的文件夹不存在则创建一个
                os.makedirs(save_path)
            if not os.path.exists(full_path): #检查文件是否存在
                r = requests.get(url, headers = headers) #设置成浏览器，防止拦截
                with open(full_path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("保存图片 "+ file_name+ " 到"+ save_path)
                r.close()
        except :
            print("爬取或者保存失败，请检查参数设置")

    def img_suffix_check(self, url, default_suffix = '.jpg'):
        suffix = ''
        try:
            for i in range(len(url)-1, 0):
                suffix += url[i]
                if(url[i] == '.'):
                    break
        except :
            pass
        if(len(suffix) <= 5 and len(suffix) >=3):
            return suffix
        else:
            return default_suffix
        
        
    def download_single_video(self, url, headers, save_path = './', file_name = ''):
        if file_name == '':
            s = url.split('.')
            file_name = s[-2][-10:-1]+'.'+s[-1]
        
        suffix_name = self.video_suffix_check(url) #提取后缀名
        if(file_name.find('.') == -1): #如果提供的文件名没有后缀名就加上一个后缀
            file_name = file_name + suffix_name
        
        full_path = os.path.join(save_path, file_name) #拼接完整的路径
        # print(full_path)
        try:
            if not os.path.exists(save_path): #保存的文件夹不存在则创建一个
                os.makedirs(save_path)
            if not os.path.exists(full_path): #检查文件是否存在
                r = requests.get(url, headers = headers) #设置成浏览器，防止拦截
                with open(full_path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("保存视频 "+ file_name+ " 到"+ save_path)
                r.close()
        except :
            print("爬取或者保存失败，请检查参数设置")
        
    def video_suffix_check(self, url, default_suffix = '.mp4'):
        suffix = ''
        for i in range(len(url)-1, 0):
            suffix += url[i]
            if(url[i] == '.'):
                break
        if(len(suffix) <= 5 and len(suffix) >=3):
            return suffix
        else:
            return default_suffix
        
        
    def download_single_others(self, url, headers, save_path = './', file_name = '', jindutiao = False):
        if file_name == '':
            s = url.split('.')
            file_name = s[-2][-10:-1]+'.'+s[-1]
        
        
        if(file_name.find('.') == -1): #如果提供的文件名没有后缀名就加上一个后缀
            suffix_name = self.video_suffix_check(url) #提取后缀名
            file_name = file_name + suffix_name
        
        full_path = os.path.join(save_path, file_name) #拼接完整的路径
        # print(full_path)
        try:
            if not os.path.exists(save_path): #保存的文件夹不存在则创建一个
                os.makedirs(save_path)
            if not os.path.exists(full_path): #检查文件是否存在
                if jindutiao == False:
                    print('尝试抓取....................')
                    r = requests.get(url, headers = headers) #设置成浏览器，防止拦截
                    print("开始保存文件 "+ file_name+ " 到"+ save_path+'..........')
                    with open(full_path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("已经保存文件 "+ file_name+ " 到"+ save_path)
                    r.close()
                else:
                    print('尝试抓取....................')
                    r = requests.get(url, headers = headers, stream=True)
                    with open(full_path, "wb") as f: #自动内存管理
                        total_length = int(r.headers.get('content-length'))
                        # print(total_length)#打印数据的大小，以字节表示
                        for ch in progress.bar(r.iter_content(chunk_size = 1024*100),label='MB', expected_size = (total_length/(1024*100)) ):
                            if ch:
                                f.write(ch)
                        f.close()
                        print("已经保存文件 "+ file_name+ " 到"+ save_path)
                
        except :
            print("爬取或者保存失败，请检查参数设置")
            
    def video_suffix_check(self, url, default_suffix = '.zip'):
        suffix = ''
        for i in range(len(url)-1, 0):
            suffix += url[i]
            if(url[i] == '.'):
                break
        if(len(suffix) <= 7 and len(suffix) >=3):
            return suffix
        else:
            return default_suffix