import ddt
import unittest
import requests
from conf.setting import TIMEOUT
from common.MyLog import log
'''
ddt 自动读文件,在类名上面 写上 @ddt.ddt
在函数上门写上 @ddt.data(参数化数据),多个参数的时候要加上 @ddt.unpack
unittest执行的时候不能直接右键执行，需要在菜单栏里点击run 然后选择python文件执行
'''
@ddt.ddt
class TestLogin(unittest.TestCase):
    @ddt.file_data('code.yml')
    @ddt.unpack
    def test_run(self,**kwargs):
        method = kwargs.get('method')
        url = kwargs.get('url')
        data = kwargs.get('data',{})
        header = kwargs.get('header',{})
        is_json = kwargs.get('is_json',0)
        check = kwargs.get('check')
        cookie = kwargs.get('cookit',{})
        try:
            if method=='post':
                if is_json:
                    r = requests.post(url,json=data,headers=header,cookies=cookie,timeout=float(TIMEOUT))
                else:
                    r = requests.post(url,data=data,headers=header,cookies=cookie,timeout=float(TIMEOUT))
            else:
                r = requests.get(url,params=data,headers=header,cookies=cookie,timeout=float(TIMEOUT))
            '''当校验很多的时候，需要用到循环'''
            for c in check:
                # print(c)
                self.assertIn(c, r.text)

        except requests.exceptions.Timeout:
            log.error(url + "请求超时")


        # self.assertEqual(check.get('error_code'),r.json().get('error_code'
if __name__ == '__main__':
    a = TestLogin()
    a.test_run()