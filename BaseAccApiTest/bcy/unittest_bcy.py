import unittest
import requests
import json

class TestStringMethods(unittest.TestCase):

    # 获取最新奖期
    def test_01(self):
        headers = {
            'Host': 'api.coinee.cc',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
            'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
        data = {
            'guessId':1,
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }

        response = requests.get('http://api.coinee.cc/upAward.json',params=data,headers=headers)
        print(json.dumps(response.json(),sort_keys=True, indent=4))


    # 用户助力全局弹窗
    def test_02(self):
        'http://api.coinee.cc/coin/userhelp/getUserHelpAlert.json?device=30&token=ac3ab162f0bdcf531a4adcf8510759e2'
        headers = {
            'Host': 'api.coinee.cc',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
            'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        data = {
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }

        response = requests.get('http://api.coinee.cc/coin/userhelp/getUserHelpAlert.json', params=data, headers=headers)
        print(json.dumps(response.json(), sort_keys=True, indent=4))

    # 个人中心
    def test_03(self):
        headers = {
            'Host': 'api.coinee.cc',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
            'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        data = {
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }
        response = requests.get('http://api.coinee.cc/user/index.json', params=data,headers=headers)
        print(json.dumps(response.json(), sort_keys=True, indent=4))

    # 获取系统时间
    def test_04(self):
        headers = {
            'Host': 'api.coinee.cc',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
            'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        data = {
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }
        response = requests.get('http://api.coinee.cc/common/time.json', params=data,headers=headers)
        print(json.dumps(response.json(), sort_keys=True, indent=4))

    # 获取比特币最新价格
    def test_05(self):
        headers = {
            'Host': 'api.coinee.cc',
            'Accept': 'application/json, text/plain, */*',
            'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
            'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        data = {
            'guessId': 1,
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }
        response = requests.get('http://api.coinee.cc/getNewestPrice.json', params=data,headers=headers)
        print(json.dumps(response.json(), sort_keys=True, indent=4))


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestStringMethods('test_01','test_02','test_03','test_04''test_05'))
    unittest.TextTestRunner(verbosity=2).run(testunit)
