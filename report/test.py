import requests
import unittest
r = requests.get('http://api-dev.westrip.com.cn/basicdata/v1.0/p/countries').text
for c in check:
    self.assertIn(c, r.text)
