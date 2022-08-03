
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:32:33 2021

@author: hp
"""

class HeadersStore():
    def __init__(self):
        self.baidu_0 = {}
        self.fill_baidu_0()
        
        self.bilibili_0 = {}
        self.fill_bilibili_0()
        
        self.project_1 = {}
        self.fill_project_1()
        
        self.simple = {}
        self.fill_simple()
        
        
        
    def get_baidu_0(self):
        return self.baidu_0
    def fill_baidu_0(self):
        self.baidu_0 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            
            'cookie':'',
            # 'Host': 'image.baidu.com',
            # 'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%D7%C4%B7&fr=ala&ala=1&alatpl=normal&pos=0',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        
    def get_bilibili_0(self):
        return self.bilibili_0
    def fill_bilibili_0(self):

        self.bilibili_0 = {
            # 'authority': 'api.bilibili.com',
            # 'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'scheme': 'https',
            # 'path': '/x/player/online/total?cid=11841141&bvid=BV1gs411Q7AE&ts=54260456',
            
            # 'origin': 'https://www.bilibili.com',
            
            # 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-fetch-dest': 'empty',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-site',
            'cookie': "_uuid=D1CAA31F-4E57-7486-814B-69A952A3505480010infoc; buvid3=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u))umYY~~|0J'uYkl|JkJm~; fingerprint=309669c81a6dc77d1c431bbafe6f22c9; buvid_fp=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; buvid_fp_plain=864C7752-54AC-4B9A-A068-9BE5FA054BCA13436infoc; sid=ananf5dj; fingerprint3=96bb62b9000e3364f50337ae13c42e3a; fingerprint_s=6193f5bd7ea1c247008b339f46e172a8; CURRENT_BLACKGAP=1; PVID=1; CURRENT_QUALITY=32; bp_video_offset_421148729=556956438230181435"
            ,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            
        }
        
    def get_project_1(self):
        return self.project_1
    def fill_project_1(self):
        self.project_1 = {
            'authority': 'www.shanghairanking.cn',
            'method': 'GET',
            'path': '/rankings/bcur/2021',
            'scheme': 'https',

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            
            'cache-control': 'max-age=0',
            'cookie': 'Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1627820563,1627872900; Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1627882471'
            ,
            
            'if-modified-since': 'Thu, 29 Jul 2021 12:36:42 GMT',
            'if-none-match': 'W/"6102a0da-21d09"',
            'referer': 'https://www.shanghairanking.cn/',
            
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        
        
    def get_simple(self):
        return self.simple
    
    def fill_simple(self):
        self.simple = {
            
            # 'cookie':'cna=w1kpGc7D4DsCAXWYTBahuohL; t=e06fa8fc2a5288ad0528b4ff158d678d; _m_h5_tk=77aed3fa0dfb5081a5d86c23da946845_1627989754665; _m_h5_tk_enc=3e23b8d498f1eb06871434145850f247; _samesite_flag_=true; cookie2=1f276408c37f307434cf00199b9b3a64; _tb_token_=3e7b37b5bd384; xlly_s=1; sgcookie=E100G6kMGLBN3zx1dPCSDt3tKDTz0bg1EpQ3dw5DePBq8qT0oOb91MRNxco7OFo5EpKs1n6z6NSk08L9YVhV3zVt0lwjjbZn4cf3ux3lzkVyZwg%3D; unb=2453636531; uc3=nk2=qh6zIy53L8LMlbum&id2=UUwVZ%2FuZ1tlF2w%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCujP8aCaylxFR7CY%3D; csg=fa999212; lgc=%5Cu795E%5Cu53A8%5Cu5C0F%5Cu798F%5Cu8D35%5Cu5947; cancelledSubSites=empty; cookie17=UUwVZ%2FuZ1tlF2w%3D%3D; dnk=%5Cu795E%5Cu53A8%5Cu5C0F%5Cu798F%5Cu8D35%5Cu5947; skt=e3d5b76f56c00e91; existShop=MTYyODIzNDY1Ng%3D%3D; uc4=id4=0%40U27KCxfR5PHtkif3AaFODob%2Bbkpg&nk4=0%40qCToO95npSOgGa%2Fw7h9qGg9wGg%2BozRg%3D; tracknick=%5Cu795E%5Cu53A8%5Cu5C0F%5Cu798F%5Cu8D35%5Cu5947; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%A5%871e; _nk_=%5Cu795E%5Cu53A8%5Cu5C0F%5Cu798F%5Cu8D35%5Cu5947; cookie1=U7U1bG0Ug3qfVHyW5DIjdSqxWvwWlT4rkCLyY5rS6wU%3D; enc=9TVR34j3pyhJo8ns5N394%2BSVB4fR8KSzA3t7kMoV9KY0tv9OA2Nb1sCF083yqn4%2FO%2FLbHQ1AnAf7UAyOO2jIPA%3D%3D; mt=ci=21_1; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&pas=0&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie14=Uoe2xeavXv0Rfw%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=97DF48DE976ED47FF898283786C14510; tfstk=cwSVBI06UoE4kMx_JntacAuxM7tAZz_1--v9oaC1KrngzKYciIh9EZLcmGOLqEf..; l=eBM_dbL7ggNDjwY9BOfwourza77tjIRAguPzaNbMiOCP9i1p5riOW6hpxmL9CnGVh60kR3ugiF-MBeYBqIv4n5U62j-lasMmn; isg=BGhoxqaYnQe9SLGDMQzizB_9OVZ6kcyb6I151yKZvOPWfQjnyqOaK1u_cRWNzYRz',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            
        }