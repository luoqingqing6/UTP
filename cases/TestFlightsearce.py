import ddt
import unittest
import requests
from common.MyLog import log
from conf.setting import BASE_URL,TIMEOUT
@ddt.ddt
class TestFlightsearce(unittest.TestCase):
    @ddt.file_data(r'D:\UTP\UTP\data\flightsearce.yml')
    @ddt.unpack
    def test_run(self,**kwargs):
        method = kwargs.get('method')
        url = BASE_URL + kwargs.get('url')
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

            for c in check:
                self.assertIn(c, r.text)

        except requests.exceptions.Timeout:
            log.error(url + "请求超时")


