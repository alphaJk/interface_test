class Animal(object):
    def run(self):
        print('animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running')
        print('这是子类')

obj = Dog()
obj.run()