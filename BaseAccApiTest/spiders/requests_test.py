import requests
import json
import time,datetime
# response = requests.get('http://httpbin.org/get')
# print(type(response))
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(type(response.text))
# print(type(response.cookies))
# print(response.cookies)

# print(response.text)
# print('content的类型是{}'.format(type(response.content)))

# data = {
#     'name':'xxx',
#     'age':22
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)

# 解析json
# print(type(response.json()))
# 格式化输出
# print(json.dumps(response.json(),sort_keys=True, indent=4))

#######获取二进制#############
# response = requests.get('https://www.github.com/favicon.ico')
# print(type(response.text))
# print(type(response.content))
# # print(response.text)
# # print(response.content)
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()

#######添加headers###########
# headers = {
#         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#
# }
#
#
# response = requests.get('https://www.zhihu.com/',headers=headers)
# print(type(response.text))
# print(response.text)

######基本POST请求##########
# data = {
#     'name':'xxx',
#     'age':'22'
# }
# headers = {
#         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#
# }
# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.text)

######状态码判断#####
# response = requests.get('http://www.jianshu.com/',headers=headers)
# print('请求失败') if not response.status_code == requests.codes.ok else print('Request Successfully')


####文件上传####
# 读取文件
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)


########获取cookies######
# response = requests.get('https://www.baidu.com')
# print(response.cookies)
#
# for key,value in response.cookies.items():
#     print('key={},value={}'.format(key,value))

#####会话维持，模拟电登录#####

# # 无效示范   解读，实际为两次不同的请求
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)
#
# # 正确示范  同一个对象发起请求，相当于在一个浏览器进行操作，维持了一个登录会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)




# data2 = {
# 'action':'queryWalletCustomerByPage&page=1&rows=20'
# }
# response2 = s.post('http://192.168.1.218:8081/wallet/customer.htm',data=data2)
# print(response2.text)


# data = {
#     'ename':'Bitcoin',
#     'device':'30',
#     'token':'ac3ab162f0bdcf531a4adcf8510759e2'
#
# }
#
# headers = {
#     'Host':'api.coinee.cc',
#     'Accept':'application/json, text/plain, */*',
#     'Cookie':'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
#     'User-Agent':'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
#     'Accept-Language':'zh-cn',
#     'Accept-Encoding':'gzip, deflate',
#     'Connection':'keep-alive',
# }
#
# response = requests.get('http://api.coinee.cc/deal/getPairByEname.json',params=data,headers=headers)
# print(json.dumps(response.json(),sort_keys=True, indent=4))


# tss1 = '2018-11-21 09:39:01'
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)

# def get_time_transformation(biz_time):
#     timeArray = time.strptime(biz_time, "%Y-%m-%d %H:%M:%S")
#     timeStamp = int(time.mktime(timeArray))
#     print(timeStamp)
#     print(type(timeStamp))
#     return timeStamp
#
#
# def get_day_time():
#     localtime = time.localtime(time.time())
#     hours = localtime[3]
#     a = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % (hours-2)
#     timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#     timeStamp = int(time.mktime(timeArray))
#     return timeStamp
#
#
#
# def compare_time(biz_time,now_time):
#     timeArray = time.strptime(biz_time, "%Y-%m-%d %H:%M:%S")
#     timeStamp = int(time.mktime(timeArray))
#     assert timeStamp>now_time,'数据时间在当前时间的两小时前'
#
#
#
# compare_time('2018-11-21 08:39:00',get_day_time())

# 自选
# data = [('action','batch'),('name','ethereum'),('name','bitcoin'),('device',30),('token','ac3ab162f0bdcf531a4adcf8510759e2')]
# response = requests.post('http://api.coinee.cc/cap/get.json',data=data)
# print(response.json())




data = {
    'ename':'Bitcoin Cash',
    'type':1,
    'device':30,
    'token':'ac3ab162f0bdcf531a4adcf8510759e2'
}
response = requests.get('http://192.168.1.220:9999/deal/getBaseCoinKline.json',params=data)
list_data = (response.json())['data']
result = list_data[len(list_data)-1]
print(result.get('bizTime'))
# print(json.dumps(response.json(),sort_keys=True, indent=4))

# data = {
#     # 'page':1,
#     'start':'2018-11-27 11:42:38',
#     'device':30,
#     'token':'ac3ab162f0bdcf531a4adcf8510759e2'
# }
#
# response = requests.get('http://api.coinee.cc/source/2/list.json',params=data)
#
# print(json.dumps(response.json(),sort_keys=True, indent=4))