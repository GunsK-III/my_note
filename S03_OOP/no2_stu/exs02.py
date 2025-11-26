# 开发一个图形绘制程序，可以处理多种形状（如圆形、矩形、三角形）。每种形状都能计算面积和周长，但计算方法各不相同。

def func02():
    # 使用函数和类型检查（不优雅，难以扩展）
    def calculate_area(shape_type, **kwargs):
        if shape_type == "circle":
            return 3.14 * kwargs["radius"] ** 2
        elif shape_type == "rectangle":
            return kwargs["width"] * kwargs["height"]
        # ... 每添加一种新形状，都要修改这个函数

    def calculate_perimeter(shape_type, **kwargs):
        if shape_type == "circle":
            return 2 * 3.14 * kwargs["radius"]
        elif shape_type == "rectangle":
            return 2 * (kwargs["width"] + kwargs["height"])
        # ...

    # 使用方式混乱，容易传错参数
    area = calculate_area("circle", radius=5)


""" 局限：
    违反开放-封闭原则：添加新形状需要修改所有处理形状的函数，容易引入错误。
    代码耦合度高：所有逻辑都集中在几个函数里，任何改动都可能产生涟漪效应。
    数据表示不清晰：用一个字典**kwargs来传递参数，缺乏结构，容易出错。"""

def object02():
    # 抽象基类（或理解为接口）
    class Shape:
        def area(self):
            raise NotImplementedError("子类必须实现此方法")

        def perimeter(self):
            raise NotImplementedError("子类必须实现此方法")

    # 具体子类
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

        def perimeter(self):
            return 2 * 3.14 * self.radius

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    # 使用：多态的威力
    shapes = [Circle(5), Rectangle(4, 6)]

    for shape in shapes:
        # 无需知道shape的具体类型，只需知道它是一个“形状”
        print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")


"""当存在一种“是一个”的层次关系，并且你希望代码能统一处理基类，而具体行为由子类决定时，必须使用类和继承。"""

