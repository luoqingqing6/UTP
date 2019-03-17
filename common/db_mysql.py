import pymysql
from conf.setting import HOST,USER,DATABASES,PASSWD
class OpMySql1:  #经典类
	pass

class OpMySql(object):#新式类
	def __init__(self,host,user,password,db,port=3306,charset='utf8'):
		schema = {
			'user':user,
			'host':host,
			'password':password,
			'db':db,
			'port':port,
			'charset':charset
		}
		try:
			self.coon = pymysql.connect(**schema)
		except Exception as e:
			print('数据库连接异常！%s'%e)
			quit('数据库连接异常！%s'%e)
		else:#没有出异常的情况下，建立游标
			self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

	def execute(self,sql):
		try:
			self.cur.execute(sql)
		except Exception as e:
			print('sql有错误%s'%e)
			return e
		if sql[:6].upper()=='SELECT':
			return self.cur.fetchall()
		else:#其他sql语句的话
			self.coon.commit()
			return 'ok'

	def __del__(self):
		self.cur.close()
		self.coon.close()

db = OpMySql(HOST,USER,PASSWD,db=DATABASES)  #实例化





