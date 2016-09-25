# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from myproject.items import MeizituItem
from scrapy.loader import ItemLoader

class MeizituSpider(scrapy.Spider):
    #整个文件的命名
    name = 'meizitu'
    #连接充许的网址后缀
    allowed_domains=['meizitu.com']
    #初始链接
    start_urls=['http://www.meizitu.com/']

    def parse(self, response):
        #抓取下一页的链接调用parse函数进行递归,直到所有页面递归完成
        sel=Selector(response)
        pages=sel.xpath("//*[@id='wp_page_numbers']/ul/li/a/@href").extract()
        page_link=pages[-2].replace('/a/','')

        # 将抓取的第一层链接反回给请求并用callback回调自身函数
        request=scrapy.Request('http://www.meizitu.com/a/%s' % page_link,callback=self.parse)
        yield request

        #接收第一层的请求响应,爬取第二层图片链接,
        sel_1=Selector(response) #解析网页
        meizi_link=sel_1.xpath("//*[@id='maincontent']/div/ul/li/div/div/a/@href").extract()
        for link in meizi_link:
            #将查询出来的图片链接list遍历出来逐一再次返回结请求,并用callback回调给函数parse_item
            request=scrapy.Request(link,callback=self.parse_item)
            yield request

    #用来提取最终网页上的信息,图片src地址
    def parse_item(self,response):
        l=ItemLoader(item=MeizituItem(),response=response)  #将itemloader实例化
        l.add_xpath("name","//*[@id='picture']/p/img/@alt")
        l.add_xpath("image_urls","//*[@id='picture']/p/img/@src")
        return l.load_item()





