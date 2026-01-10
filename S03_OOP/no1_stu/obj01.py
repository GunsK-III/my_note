# 第一课

class Person:
    # 类常量 - 所有实例共享，不能修改
    SPECIES = "人类"

    # 类变量 - 所有实例共享，可以修改
    some_count = 0
    _total_count = 0  # 私有类变量（约定）

    def __init__(self, name, age):
        """构造器/初始化方法 - 创建实例时自动调用"""
        # 实例变量 - 每个实例独有
        self.name = name  # 公共实例变量
        self.age = age    # 公共实例变量
        self.__id = self._generate_id()  # 私有实例变量（双下划线）

        # 更新类变量
        Person._total_count += 1

    def _generate_id(self):
        """私有方法（约定，非强制）"""
        import time
        return int(time.time() * 1000) % 10000

    def introduce(self):
        """实例方法 - 可以访问实例变量和类变量"""
        return f"我叫{self.name}，今年{self.age}岁，属于{Person.SPECIES}"

    @classmethod
    def get_total_count(cls):
        """类方法 - 只能访问类变量，不能访问实例变量"""
        return f"总共有{cls._total_count}个人被创建"

    @staticmethod
    def is_adult(age):
        """静态方法 - 与类相关但不需要访问类或实例变量"""
        return age >= 18

    # 属性装饰器 - 将方法转为属性访问
    @property
    def id(self):
        """只读属性 - 可以像变量一样访问"""
        return self.__id


# 使用示例
if __name__ == "__main__":
    # 1. 实例化 - 创建类的实例
    person1 = Person("张三", 25)  # 调用 __init__ 方法
    person2 = Person("李四", 17)

    # 2. 访问实例变量
    print(person1.name)  # 输出: 张三
    print(person2.age)   # 输出: 17
    # print(person1.__id)  # 尝试访问私有变量 >> AttributeError

    # # 3. 调用实例方法
    # print(person1.introduce())  # 输出: 我叫张三，今年25岁，属于人类
    #
    # # 4. 访问类常量
    # print(Person.SPECIES)  # 输出: 人类
    # # Person.SPECIES = "新人类"    # 不应该这样做（虽然技术上可以）
    #
    # # 5. 调用类方法
    # print(Person.get_total_count())  # 输出: 总共有2个人被创建
    #
    # # 6. 调用静态方法
    # print(Person.is_adult(20))  # 输出: True
    # print(person1.is_adult(16))  # 输出: False
    #
    # # 7. 访问属性（看起来像变量，实际上是方法调用）
    # print(f"ID: {person1.id}")  # 输出: ID: 1234 (示例值)
    #
    # # 8. 尝试访问私有变量（不建议直接访问）
    # # print(person1.__id)          # 会报错: AttributeError
    # # print(person1._Person__id)   # 可以访问但不推荐（名称修饰）
    #
    # # 9. 访问私有类变量（约定）
    # print(f"通过类访问: {Person._total_count}")
    #
    # # 10. 修改实例变量
    # person1.age = 26
    # print(person1.age)  # 输出: 26
