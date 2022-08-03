import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    # start_urls = ['http://python123.io/ws/demo.html']
    start_urls = ['https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%BB%BA%E7%AD%91']

    def parse(self, response):
        fname = 'demo.html'
        with open(fname, 'wb') as f:
            f.write(response.body.encode('utf8'))
        self.log("Save file %s" % fname)
        
