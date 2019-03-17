import sys,os
import time

BASE_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
sys.path.insert(0,BASE_PATH)#加入到环境变量，放在list首位，当然用append也可以
from common.tools import GetCase
from conf.setting import PY_PATH,REPORT_PATH#导入用例所在目录，报告目录
import unittest,BeautifulReport
def run():
    g = GetCase()
    g.creat_py()#生成测试文件
    suite = unittest.TestSuite()#生成测试套件把所有用例加进来
    all_cases = unittest.defaultTestLoader.discover(PY_PATH,'Test*.py')#discover找测试用例的
    [suite.addTests(case) for case in all_cases]#把测试用例条件到套件
    report_obj = BeautifulReport.BeautifulReport(suite)#执行用例
    fmt = '{date}_TestReport.html'.format(date=time.strftime('%Y%m%d-%H_%M_%S'))
    report_obj.report(filename=fmt,log_path=REPORT_PATH,description='utp测试报告')#生成报告

run()
