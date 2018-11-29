

class PrivateTest():
    test_name=0
    def __init__(self,str1,str2):
        self.__private_name=str1
        self.__test='str2'

    def __private_fun(self):
        print('我是私有方法1')

    def __private_fun2(self):
        print('开始调用私有方法1')
        self.__private_fun()
        print('我是私有方法2')
        # print(self.__private_name)

    def foo(self):
        print(self.__class__.test_name)
        print('调用了共有方法')
        print('下面调用的是私有方法')
        # self.__private_fun()
        self.__private_fun2()
        print(self.__private_name)

obj = PrivateTest('私有变量1','私有变量2')
# print(obj.__private_name)
# obj.__private_name = 1
# print(obj.__private_name)
obj.foo()




print(dir(obj))