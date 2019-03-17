import logging
from logging import handlers
from conf.setting import LOG_PATH
class Logger(object):
	level_relations = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'crit': logging.CRITICAL
	}  # 日志级别关系映射
	def __init__(self,filename,level='debug',
				 when='D',
				 back_count=3,
				 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
		self.logger = logging.getLogger(filename)
		# 分割日志的单位 S 秒、M 分、 H 小时、 D 天、 W 每星期（interval==0时代表星期一）、midnight 每天凌晨

		format_str = logging.Formatter(fmt) #设置日志格式
		self.logger.setLevel(self.level_relations.get(level)) #设置日志级别
		#需要根据level_relations字典使用get方法去取值
		sh = logging.StreamHandler()
		sh.setFormatter(format_str)
		th = handlers.TimedRotatingFileHandler(filename=filename,when=when,
											   backupCount=back_count,encoding='utf-8')
		th.setFormatter(format_str)
		self.logger.addHandler(sh)
		self.logger.addHandler(th)


log = Logger(LOG_PATH).logger
#直接在本文件里面实例化，用的时候导入log就行了，不需要再实例化了

if __name__ == '__main__':
	log = Logger('nhyXXX.log')
	log.logger.debug('i的是100')
	log.logger.info('开机')
	log.logger.warning('警告 飞机没油了')
	log.logger.error('错误 飞机要爆炸')