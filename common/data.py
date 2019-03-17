import sys,os
import time
from conf.setting import DAY,REPORT_PATH

class Testdata(object):

    def timestampToStr(self,is_second):  # 时间戳转格式化好的时间
        old_time = int(time.time()) + DAY
        cur_time = time.localtime(old_time)# 时间戳转成时间元组
        if is_second:
            res = time.strftime("%Y-%m-%d %H:%M:%S", cur_time)  # 再把时间元组转成格式化好的时间
        else:
            res = time.strftime("%Y-%m-%d", cur_time)
        return res

    # def clean_log(self,REPORT_PATH):
    #     #获取三天前时间戳,86400为1天的秒数
    #     old_time = int(time.time()) - 86400 * DAY
    #     s = int(timestampToStr(True,old_time))
    #     for filename in os.listdir(REPORT_PATH):
    #         log_data = filename.split('-')[1]
    #         new_log_data = int(''.join(log_data.split('-')))
    #         if s >= new_log_data:
    #             os.remove(REPORT_PATH +'\\'+filename)
    #      print('过期日志已经清理')



# def param():
#     args = sys.argv
#     if len(args)>1:
#         path = args[1]
#         if os.path.isdir(path):#判断是否是路径
#             clean_log(path)
#         else:
#             print('必须传目录！')
#     else:
#         print('运行这个python文件需要传入一个路径!\n'
#               '运行示例： python clean_log.py /usr/tomcat/logs')

# param()