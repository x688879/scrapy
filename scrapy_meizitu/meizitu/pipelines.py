# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImagePipeline(ImagesPipeline):
    #下载图片,将遍历出来图片src和item中的数据返回给请求
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'name':item['name'],'image_url':item['image_urls']})

     #将图片路径为空的去掉
    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("item contains no images")
        item['image_paths']=image_paths
        return item

    #更改文件的名字:将item 中的image_urls和name形成字典,然后用request.url来查询name进行名字替换
    def file_path(self, request, response=None, info=None):
        image_url=request.meta['image_url']
        image_name=request.meta['name']
        image_url_name_dict=dict(zip(image_url,image_name))
        image_guid=image_url_name_dict[request.url]
        return 'full/%s.jpg' % image_guid


