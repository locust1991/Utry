#!/usr/bin/python
# coding: utf-8

from HTMLParser import HTMLParser


class GetTitleSpider(HTMLParser):

	def __init__(self):
		self.title = ''
		self.topic = ''
		self.source = ''
		self.readingtitle = 0
		HTMLParser.__init__(self)

	def handle_starttag(self,tag,attrs):
		if tag == 'title':
			self.readingtitle=1

	def handle_data(self, data):
		if self.readingtitle:
			tmp = data.split(' _ ')
			if len(tmp) > 0:
				self.title += tmp[0]
			if len(tmp) > 1:
				self.topic = tmp[1]
			if len(tmp) > 2:
				self.source= tmp[2]

	def handle_endtag(self, tag):
		if tag == 'title':
			self.readingtitle=0
	
	#返回主标题
	def gettitle(self):
		return self.title
	
	#返回主题
	def gettopic(self):
		return self.topic

	#返回来源
	def getsource(self):
		return self.source





		
		
