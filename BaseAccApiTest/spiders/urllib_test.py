import urllib.request
import urllib.parse
import socket
import urllib.error


'''urllib基本用法
'''
# get请求
# response = urllib.request.urlopen('http://www.baidu.com/')
# # bytes转换为字符串
# print(response.read().decode('utf-8'))

# post请求
# data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 异常捕获
# 在一秒之内响应不会报错
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("TIME OUT")


######### 响应 #########
# 响应类型
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.read().decode('utf-8'))


# Request
# request = urllib.request.Request('https://www.python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
#     'Host':'httpbin.org'
# }
#
# dict = {
#     'name':'Germey'
# }
# data = bytes(urllib.parse.urlencode(dict),encoding='utf8')
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# # req.add_header('')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))