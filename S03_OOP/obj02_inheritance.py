# 父类：动物
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}正在吃东西")

    def sleep(self):
        print(f"{self.name}正在睡觉")

# 子类1：狗
class Dog(Animal):
    def bark(self):
        print(f"{self.name}汪汪叫")

    # 重写父类的方法（多态）
    def eat(self):
        print(f"{self.name}正在津津有味地吃狗粮")

# 子类2：猫
class Cat(Animal):
    def meow(self):
        print(f"{self.name}喵喵叫")

    def eat(self):
        print(f"{self.name}优雅地吃猫粮")


# 创建对象
animal = Animal("小动物")
dog = Dog("旺财")
cat = Cat("咪咪")

# 继承的特性展示
print("=== 动物的行为 ===")
animal.eat()
animal.sleep()

print("\n=== 狗的行为 ===")
dog.eat()      # 继承并重写了父类方法
dog.sleep()    # 直接继承父类方法
dog.bark()     # 子类特有的方法

print("\n=== 猫的行为 ===")
cat.eat()      # 继承并重写了父类方法
cat.sleep()    # 直接继承父类方法
cat.meow()     # 子类特有的方法
