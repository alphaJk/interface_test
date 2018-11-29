import requests
import json
from urllib import parse
from urllib import request


headers = {
    'Host':'api.coinee.cc',
    'Accept':'application/json, text/plain, */*',
    'Cookie':'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
    'User-Agent':'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
    'Accept-Language':'zh-cn',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
}



data = {
    'roomKey':'3a4f9f32LNGd1a1ff46c70a4ceea2e2152ba01d797f',
    'device':'30',
    'token':'ac3ab162f0bdcf531a4adcf8510759e2'

}


# data = {
#     'gameConfId':52,
#     'type':2,
#     'device':'30',
#     'token':'ac3ab162f0bdcf531a4adcf8510759e2'
# }


response = requests.get('http://api.coinee.cc/game/match/getGame.json',params=data,headers=headers)
# response = requests.get('http://api.coinee.cc/game/match/usermatchgame.json',params=data,headers=headers)
print(json.dumps(response.json(),sort_keys=True, indent=4))
# url_data = '%E5%A4%8F%E5%A4%A9'
# url_org = parse.unquote(url_data)
# print(url_org)


