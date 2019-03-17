import os
BASE_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
CASE_PATH = os.path.join(BASE_PATH,'data')#用例目录
LOG_PATH = os.path.join(BASE_PATH,'logs','utp.log')#日志目录
REPORT_PATH = os.path.join(BASE_PATH,'report')#报告目录
CASE_EG = os.path.join(BASE_PATH,'conf','base_case.eg')#用例模板
PY_PATH = os.path.join(BASE_PATH,'cases')#利用模板和生成的Python文件放在这个目录下

#定义测试接口的URL
BASE_URL = 'http://api-dev.westrip.com.cn'
# HEADER = {"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI1NSIsIm9wVXNlck5hbWUiOiLmtYvor5UwMTIiLCJleHAiOjE1NTIzOTE5MTAsImlhdCI6MTU1MjM4NTkxMH0.qxPOnmrdD8RcYIeC9VAXgkBwWvRPTSUF_FRmT3vNyiehFwP6SLeE10lQSBpka3tY5GH5h00FxeLqiDLqVa6LEw"}

#天数
DAY = 86400*3
#MySQL配置
HOST = '123.206.22.46'
USER = 'westrip'
PASSWD = 'xiyouji!@#$%%20180728'
DATABASES = 'westrip'

#超时设置
TIMEOUT = 10

# #发送邮件配置
#
# USERNAME = '1757710953@qq.com'
# PASSWD = 'luo139'
# REVE=[1757710953@qq.com]
# TITLE = '测试报告'
# CONTENT = '测试报告'






