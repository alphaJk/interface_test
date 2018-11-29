import time
import datetime
import uuid
import string

SECRET_KEY = "DebugTalk"


def get_time():
    nowtime=lambda:int(round(time.time() * 1000))
    data=nowtime()
    return data


def get_start_time():
    sevenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=7))
    startTime=sevenDayAgo.strftime("%y-%m-%d")
    return startTime


def get_end_time():
    endTime=time.strftime("%y-%m-%d",time.localtime())
    return endTime


def create_uuid():
    uid=str(uuid.uuid4())
    data=''.join(uid.split('-'))
    return data


'''生成uuid，每两个一组，每组内的uuid相同
'''
old_uuid = ""
count = 1
def create_serial_number():
    global old_uuid
    global count
    uuid = old_uuid
    if (count%2) == 1:
        uuid = create_uuid()
        old_uuid = uuid
    count+=1
    return uuid

'''获取比当前时间早两小时的时间戳
'''
def get_day_time():
    localtime = time.localtime(time.time())
    hours = localtime[3]
    a = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % (hours-2)
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


# 日k使用，昨天凌晨零点的时间戳
def get_zero_time():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    yesterday_zero_time = int(time.mktime(yesterday.timetuple()))
    return yesterday_zero_time


# 获取格式化的当前时间
def get_time_str():
    result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return result


# 周k使用，获取上周一零点的时间
def get_monday():
    # 获取当前时间，小时，分，秒，毫秒改为0
    today = datetime.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
    # 获取当前星期的表示，星期一为0，周日为6
    days = today.weekday()
    # 距离上周一时间差值
    x_day = datetime.timedelta(days=(days + 7))
    # 获取上周一的时间
    result = (today - x_day).timetuple()
    result2 = round(time.mktime(result))
    return result2



# 月k使用，获取上个月的1号时间
def get_month_zero_time():
    result = (datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)
    timeArray = time.strptime(str(result), "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


'''编写自定义断言
    GT 就是 GREATER THAN 大于　
    GE 就是 GREATER THAN OR EQUAL 大于等于  
    LT 就是 LESS THAN 小于 
    LE 就是 LESS THAN OR EQUAL 小于等于
'''


# 报价接口数据的最新时间对比
def compare_time(data,now_time):
    dict_len = len(data)
    for i in range(dict_len):
        dict_data = data[i].get('bizTime')
        timeArray = time.strptime(dict_data, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        assert timeStamp > now_time, '数据时间在当前时间的两小时前'


# 货币日k最新数据对比
def day_kline_compare(data,yesterday_zero_time):
    list_len = len(data)
    bizTime = data[list_len-1].get('bizTime')
    timeArray = time.strptime(bizTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    assert timeStamp == yesterday_zero_time, '10点30后，昨日的日k没有生成'


# 周k数据时间对比
def week_kline_compare(data,monday_time):
    list_len = len(data)
    bizTime = data[list_len - 1].get('bizTime')
    timeArray = time.strptime(bizTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    assert timeStamp == monday_time, '上周一时间'


# 月k数据时间对比
def month_kline_compare(data,month_zero_time):
    list_len = len(data)
    bizTime = data[list_len - 1].get('bizTime')
    timeArray = time.strptime(bizTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    assert timeStamp == month_zero_time, '上个月1号的时间'







