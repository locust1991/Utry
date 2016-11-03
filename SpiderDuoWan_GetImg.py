#!/usr/bin/python
#coding: utf-8

#re正则表达块
import re
import urllib2

class GetDuoWanImg:
    # self表示构造函数创建的对象
    def __init__(self):
        self.img = []

    #请求url 方式二,获取网页内容
    def GetContext(self,url):
        request = urllib2.Request(url)#用url获取一个request对象
        response = urllib2.urlopen(request)#返回一个response对象，如同一个文件对象
        img_data = response.read()#读取html中的数据
        return img_data

    def getImg(self, content):
    	patten = re.compile('<div id=\"text\">.+',re.S)#加入re.S匹配包含换行符
    	imgtext = re.findall(patten,content)
    	if len(imgtext)>0:
    		imglist = re.findall(r'http:.+\.png',imgtext[0])
    	else:
    		imglist = ''
    	return imglist

    
