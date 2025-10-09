# 私有变量
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


class Number:
    def __init__(self):
        self.pub_num = 1
        self.__pri_num = 1

    def pub_method(self):
        a = self.__pri_num
        return a


num = Number()
print(num.pub_num)
print(num.pub_method())


















