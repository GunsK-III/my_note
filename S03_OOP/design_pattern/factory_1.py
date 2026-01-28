""" 工厂模式（Factory Pattern）是 Python 中常用的一种 创建型 设计模式，
    它的核心思想是：将对象的创建过程封装起来，使客户端代码无需关心具体类的实例化细节。
    在程序开发中，我们常常需要根据不同的条件创建不同类型的对象。
    工厂模式通过引入一个“工厂”来统一管理对象的创建，使得新增产品类型时，只需修改工厂，而不用改动客户端代码。"""


# 简单工厂（Simple Factory）【非 GoF 23 种之一，但很常用】
class Dog:
    @staticmethod
    def speak():
        return "Woof!"

class Cat:
    @staticmethod
    def speak():
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal")


animal = animal_factory("dog")
print(animal.speak())       # >> Woof!
