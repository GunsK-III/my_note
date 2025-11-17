# 类继承
# class Person:
#     def __init__(self, name: str, sex: str, age: int):
#         self.name = name  # 属性
#         self.sex = sex
#         self.age = age
#         self.num_eyes = 2
#
#     def breath(self):  # 方法
#         return f"{self.name}可以呼吸。"
#
#
# class Man(Person):
#     def __init__(self, name, sex, age):
#         super().__init__(name=name, sex='男', age=age)
#         self.characteristic = "有胡子"
#
#
# class Woman(Person):
#     def __init__(self, name, sex, age):
#         super().__init__(name, sex, age)
#         self.characteristic = "没胡子"
#
#
# ming = Man("小明", "男", 18)
# mei = Woman("小美", "女", 18)
#
# print(ming.name, ming.breath(), ming.characteristic)
# print(mei.name, mei.characteristic)


# ---------------------------------------------------
class Worker:
    def __init__(self, name, worker_id):
        self.name = name
        self.worker_id = worker_id

    def get_info(self):
        return f"{self.name}的工号是{self.worker_id}"


class FillTimeWorker(Worker):  # 全职
    def __init__(self, name, worker_id):  # 对象输入的参数
        super().__init__(name, worker_id)  # 对象继承的参数
        self.work_class = "全职"
        self.monthly_salary = 3500

    def get_salary(self):
        return f"全职工{self.name}的月薪是{self.monthly_salary}"


class PartTimeWorker(Worker):  # 兼职
    def __init__(self, name, worker_id, days):
        super().__init__(name, worker_id)
        self.work_class = "兼职"
        self.daily_salary = 100
        self.days = days

    def get_salary(self):
        return f"兼职工{self.name}的兼职收入是{self.daily_salary * self.days}"


ming = FillTimeWorker("小明", "001")
salary_ming = ming.get_salary()
print(salary_ming)
