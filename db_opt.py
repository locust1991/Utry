#!/usr/bin/python
# coding: utf-8
import MySQLdb
#数据库操作类
class opt_db:
	#获取数据库连接
	def get_con(self):
		try:
			cnn=MySQLdb.connect(host='localhost',user='spider',passwd='123456',db='spider',port=3306,charset='utf8')
			return cnn
		except MySQLdb.Error,e:
			print "MySQLdb Error:%s" % e

	#查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典 
	def select(self,sql):
		try:
			con = self.get_con()
			cur = con.cursor(MySQLdb.cursors.DictCursor)
			count=cur.execute(sql)
			fc=cur.fetchall()
			return fc
		except MySQLdb.Error,e:
			print "Mysqldb Error:%s" % e
		finally:
			cur.close()
			con.close()
	
	#更新操作
	def update(self,sql,para):
		try:
			con=self.get_con()
			cur=con.cursor()
			count=cur.execute(sql,para)
			con.commit()
			return count
		except MySQLdb.Error,e:
			con.rollback()
			print "Mysqldb Error:%s" % e
		finally:
			cur.close()
			con.close()

