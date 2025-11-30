# 三元表达式/条件表达式，根据一个条件的真假，从两个表达式中选择一个值。
# 基本语法：value_if_true if condition else value_if_false。
# 三元表达式只需1行就能完成 if-else 至少4行的表达，这是更 pythonic 的写法。

def exs01():
    """基本数字比较"""
    # 使用传统的 if-else 语句
    age = 18
    if age >= 18:
        status = "成年"
    else:
        status = "未成年"
    print(status)  # >> 成年

    # 使用三元表达式
    age = 18
    status = "成年" if age >= 18 else "未成年"
    print(status)  # >> 成年


def exs02():
    """找出两个数中的较大值"""
    a = 10
    b = 20
    # 传统写法
    if a > b:
        max_num = a
    else:
        max_num = b
    print(max_num)

    # 三元表达式写法
    max_num = a if a > b else b
    print(max_num)  # 输出：20


def exs03():
    """在函数返回值中使用"""
    def get_absolute_value(x):
        # 如果 x >= 0，返回 x；否则返回 -x
        return x if x >= 0 else -x

    print(get_absolute_value(5))    # >> 5
    print(get_absolute_value(-3))   # >> 3


def exs04():
    """在列表推导式中使用"""
    # 将一个列表中的数字转换为 "偶数" 或 "奇数"
    numbers = [1, 2, 3, 4, 5]
    result = ["偶数" if x % 2 == 0 else "奇数" for x in numbers]
    print(result)  # >> ['奇数', '偶数', '奇数', '偶数', '奇数']


def exs05():
    """嵌套（生产中最好不要嵌套）"""
    # 传统的 if-elif-else 结构
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(grade)

    # 三元表达式
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(grade)  # >> B

