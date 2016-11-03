#!/usr/bin/python
# coding: utf-8
import sys
from urllib import urlopen
from SpiderDuoWan_GetTitle import GetTitleSpider
from SpiderDuoWan_GetImg import GetDuoWanImg

from db_opt import opt_db

#重新设置字符集（）
reload(sys)
sys.setdefaultencoding('utf-8')

#请求url 方式一，获取网页内容
url='http://lol.duowan.com/1610/341574528881.html'
text=urlopen(url).read()
url_obj = GetTitleSpider()
url_obj.feed(text)#调用解析器
url_obj.close()

'''
print url_obj.gettitle()
print url_obj.gettopic()
print url_obj.getsource()
'''

#请求url 方式二,获取网页内容
#sql='select * from spider.spider_news'

#获取图片的url
img_obj = GetDuoWanImg();
img_data = img_obj.GetContext(url)
img_url =img_obj.getImg(img_data)

#获取url中的文章主题
title = url_obj.gettitle()#获取标题
topic = url_obj.gettopic()#获取主题
source = url_obj.getsource()#获取来源

#获取数据库操作对象
db=opt_db()

#数据处理，更新表中的数据
sql="insert into spider.spider_news(title,topic,source,context_img_url,`update`) values(%s,%s,%s,%s,now())"
para=(title,topic,source,str(img_url))
db.update(sql,para)