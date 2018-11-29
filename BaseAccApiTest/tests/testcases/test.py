# import uuid
import datetime
import time
import calendar
import random

# today = datetime.date.today()
# today_time = int(time.mktime(today.timetuple()))
# print(today_time)
# result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(result)






# result = (datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)
# timeArray = time.strptime(str(result), "%Y-%m-%d")
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)


#
#
# def create_uuid():
#     uid=str(uuid.uuid4())
#     data=''.join(uid.split('-'))
#     return data
#
#
# oldUuid=""
# count=1
#
# def randomxx():
#     global oldUuid
#     global count
#     uuid = oldUuid
#     if (count%2) == 1:
#         uuid = create_uuid()
#         oldUuid = uuid
#     count+=1
#     print(uuid)
#
#
# for i in range(10):
#     randomxx()


# print('前面的函数') if not 1==2 else print('后面的函数')




# m1 = calendar.MONDAY
# print(m1)



# def get_monday(today):
#     # today = datetime.datetime.today()
#     days = today.weekday()
#     x_day = datetime.timedelta(days=(days + 7))
#     result = today - x_day
#     print(result)

# today = datetime.datetime.today()
# print(today)
# print(type(today))
# print(today.weekday())



#
# date1 = (2018,1,1,0,0,0,-1,-1,-1)
# time1 = time.mktime(date1)
# date2 = (2018,11,1,0,0,0,-1,-1,-1)
# time2 = time.mktime(date2)
#
# # print(time1)
#
# random_time = random.uniform(time1,time2)
# result = datetime.datetime.utcfromtimestamp(random_time)
# # print(type(result))
# print(result)
#
# get_monday(result)


def get_monday():
    today = datetime.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
    days = today.weekday()
    x_day = datetime.timedelta(days=(days + 7))
    result = (today - x_day).timetuple()
    result2 = round(time.mktime(result))
    print(result2)
    return result2
get_monday()