"""
    lambda 参数: 表达式
    · 可以有多个参数，用逗号分隔。
    · 冒号后面只能是一个表达式（不能是语句，比如不能有 print、return、if...else 多行逻辑等）。
    · 表达式的计算结果会自动作为函数的返回值。
"""

def exs01():
    """ 简单示例 """
    string = lambda: "Hello, world!"
    print(string())  # >> Hello, world!
    x = lambda a: a + 10
    print(x(5))


# lambda 最常用于需要一个简单函数作为参数的场景
def exs02():
    """ 与map()一起使用 """
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)    # >> [1, 4, 9, 16]

def exs03():
    """ 与filter()一起使用 """
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)      # >> [2, 4, 6]

def exs04():
    """ 与sort()一起使用 """
    students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
    # 按成绩排序
    sorted_students = sorted(students, key=lambda student: student[1])
    print(sorted_students)      # >> [('Charlie', 78), ('Alice', 85), ('Bob', 90)]

