""" 数字类型：int、float、complex、bool
    数字类型均是不可变类型，此外不可变类型还有：字符串、元组
    不可变类型一经创建不可修改，若要修改值得创建新对象再引用"""
import math, decimal


def exs01():
    """运算"""
    var1, var2 = -1.16, 1.16
    print(abs(var1))                # 绝对值。>> 1.16
    print(math.ceil(var1), math.ceil(var2))             # 上取整。>> 1 2
    print(math.exp(0))              # 返回e的次幂
    print(math.log(math.e), math.log(100, 10))  # 对数。>> 1.0 2.0
    print(math.log10(100))          # 10的对数。>> 2.0
    print(math.pow(2, 3))           # 幂。>> 8.0
    print(round(var2, 1))           # round() 四舍六入五成双
    print(math.sqrt(4))             # 开方


def exs02():
    """保留小数位数"""
    # round()函数
    print("pi:", math.pi, "\t", "e:", math.e)
    print(round(math.pi))           # >> 3
    print(round(math.pi, 2))        # >> 3.14。类型是浮点数

    # f-string
    print(f"{math.pi:.2f}")         # >> 3.14。类型是字符串

    # format 格式化方法
    print("{:.2f}".format(math.pi)) # >> 3.14

    # % 格式化
    print("%.2f" % math.pi)


def exs03():
    """浮点数精度"""
    num1 = 1.3 + 2.6
    print(num1)         # >> 3.9000000000000004（不同计算机结果不一致）
    num2 = decimal.Decimal('1.3') + decimal.Decimal('2.6')
    print(num2)         # >> 3.9


exs03()
