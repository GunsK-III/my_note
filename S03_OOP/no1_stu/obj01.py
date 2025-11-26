# 第一课
class Cat:
    def __init__(self, name, color, age):
        """通过__init__这个构造方法初始化实例变量，也就是创建对象、定义对象有哪些属性、对属性赋值"""
        self.name = name
        self.color = color
        self.age = age

    def speak(self):
        """这里定义对象拥有的方法，方法表示对象能做什么事"""
        """在__init__中，self表示对象自身，self可以把属性值绑定到对象自身上
           在方法中，self可以让人在方法中获取、修改对象的属性 """
        print(self.age * "喵")

    def think(self, content):
        print(f"{self.name}在想{content}")


Cat("AA", "白色", 2).speak()  # 这里调用类方法，并传入参数
Cat("BB", "黑色", 3).think("吃吃吃")


# class Stu:
#     def __init__(self, name: str, stu_id: str, yu: int, shu: int, ying: int):
#         self.name = name
#         self.stu_id = stu_id
#         self.marks = {"语": yu, "数": shu, "英": ying, "其它": 0, "附加": 0}
#
#     def set_mark_other(self, info, mark):
#         self.marks[info] = mark
#
#
# stu1 = Stu("张三", "2019001", 90, 80, 70)
# Stu.set_mark_other(stu1, "附加", 100)
# Stu.set_mark_other(stu1, "其它", 100)
#
# print(stu1.marks)

