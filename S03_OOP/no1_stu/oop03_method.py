""" 方法 method
    1. 初始化方法 >> 一种特殊方法/魔术方法
    2. 实例方法 >> 最常用
    3. 静态方法 >> 与类相关但不需要访问类或实例数据
    4. 类方法 >>
    5. 属性方法
"""


class Class3:
    num0 = 1

    def __init__(self):  # 初始化方法
        self.num1 = 123  # 实例变量

    def method1(self):  # 实例方法
        self.num1 = 12  # 可以修改实例变量

    @staticmethod
    def method2():      # 静态方法
        num2 = 123
        return num2

    @classmethod
    def method3(cls):   # 类方法
        """ 类方法：只能访问类，不能访问实例
            1. 替代构造器 - 无需实例就能创建对象
            2. 操作类变量 - 无需创建实例就能获取类信息 """
        num0 = 100


print(Class3().num1)
cls1 = Class3()     # 创建实例
cls1.method1()      # 调用方法
print(cls1.num1)    # 通过实例访问num1。 >> 12
print(Class3.method2())     # 可以调用静态方法  >> 123
cls1.method3()
print(Class3.num0)
