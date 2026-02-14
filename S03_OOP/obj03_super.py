class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal的init方法：{name}出生了")

    def eat(self):
        print(f"{self.name}正在吃东西")


class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的__init__方法
        super().__init__(name)
        self.breed = breed
        print(f"Dog的init方法：这是一只{breed}")

    def eat(self):
        # 调用父类的eat方法
        super().eat()
        print(f"{self.name}吃完后摇尾巴")


dog = Dog("旺财", "金毛")
print("---")
dog.eat()
