# -*- coding: utf-8 -*-
item={'image_paths': [u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg',
                 u'full/\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20.jpg'],
 'image_urls': [u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/01.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/02.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/03.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/04.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/05.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/06.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/07.jpg',
                u'http://pic.meizitu.com/wp-content/uploads/2016a/07/29/08.jpg'],
 'name': [u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c1\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c2\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c3\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c4\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c5\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c6\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c7\u5f20',
          u'\u5f88\u706b\u7684\u5185\u8863\uff0c\u7b2c8\u5f20']}


dic=dict(zip(item['image_urls'],item['name']))
i_1='http://pic.meizitu.com/wp-content/uploads/2016a/07/29/01.jpg'
print dic[i_1]
