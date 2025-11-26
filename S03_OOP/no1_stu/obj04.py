class Animal:
    def __init__(self, name):
        self.name = name  # 实例属性

    def speak(self):
        raise NotImplementedError("子类必须实现此方法")

    @classmethod        # 声明此方法是类方法
    def from_birth_year(cls, name, birth_year):
        # 类方法常用于替代构造函数
        current_year = cls._current_year()
        age = current_year - birth_year
        return cls(name)

    @staticmethod       # 静态方法
    def _current_year():
        # 静态方法：不依赖实例或类
        import datetime
        return datetime.datetime.now().year

    def __str__(self):
        return f"Animal(name={self.name})"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# 使用示例
dog = Dog("Buddy")
cat = Cat.from_birth_year("Whiskers", 2019)

print(dog.speak())  # 输出: Buddy says Woof!
print(cat.speak())  # 输出: Whiskers says Meow!

print(dog)  # 输出: Animal(name=Buddy)
