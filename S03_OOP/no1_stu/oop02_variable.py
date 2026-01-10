""" 类变量 Class Variable
    1. 类的常量
    2. 类的公共变量 > 可以在任何地方访问
    3. 类的受保护变量 > 子类可以访问，但外部不建议直接访问
    4. 类的私有变量 > 只允许类内部访问
    5. 类的实例变量 """

class Class2:
    # 类常量 - 所有实例共享，不能修改
    NUM1 = 12

    # 类变量 - 所有实例共享，可以修改
    num2 = 123
    _num3 = 1234     # 私有类变量（约定），这是一个内部实现细节，不应该直接访问
    __num4 = 12345   # 私有类变量（强制）

    def __init__(self):
        self.num5 = 123456    # 实例变量 - 通过创建实例，可以访问


print(Class2.NUM1)
print(Class2.num2)
print(Class2._num3)
# print(Class2.__num4)    # AttributeError
print(Class2.__dict__)
# >> {'__module__': '__main__', 'NUM1': 12, 'num2': 123, '_num3': 1234, '_Class1__num4': 12345,...}
num5 = Class2().num5
print(num5)
