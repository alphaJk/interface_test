from locust import HttpLocust, TaskSet, task
'''locust配置和启动
'''


class UserBehavior(TaskSet):
    headers = {
        'Host': 'api.coinee.cc',
        'Accept': 'application/json, text/plain, */*',
        'Cookie': 'JSESSIONID=35AC586927C99C8C537B459E18095A2E',
        'User-Agent': 'BiCiYuan/7 CFNetwork/975.0.3 Darwin/18.2.0',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }


    @task
    def get_newest_price(self):
        data = {
            'guessId': 1,
            'device': '30',
            'token': 'ac3ab162f0bdcf531a4adcf8510759e2'
        }
        self.client.get("http://api.coinee.cc/getNewestPrice.json",params=data,headers=self.headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0  # ms
    max_wait = 1


'''
locust --host=http://localhost:8089
'''

