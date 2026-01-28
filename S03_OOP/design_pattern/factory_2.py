# 工厂方法模式（Factory Method Pattern）
# 符合开闭原则，易于扩展，每个产品对应一个工厂，结构清晰

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 工厂基类
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# 客户端代码
def client_code(factory: AnimalFactory):
    animal = factory.create_animal()
    print(animal.speak())


client_code(DogFactory())  # >> Woof!
client_code(CatFactory())  # >> Meow!
