"""高阶函数（Higher-order function）是指能够接收一个或多个函数作为参数，或者返回一个函数作为结果的函数。
在数学和计算机科学中，高阶函数是一个非常重要的概念，因为它们允许我们以更抽象和灵活的方式来编写代码。"""

def exs01():
    """基础用法"""
    def adds(x, y, f):
        return f(x) + f(y)

    res = adds(-5, 6, abs)
    print(res)       # >> 11


def exs02():
    """map()函数。将函数应用于可迭代对象的每个元素"""
    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    print(f"map() 函数演示:")
    print(f"原始列表: {numbers}")
    print(f"平方后的列表: {squared_numbers}")     # >> [1, 4, 9, 16, 25]


def exs03():
    """filter()函数。在可迭代对象中，过滤出满足条件的元素"""
    def is_even(x):
        return x % 2 == 0        # 判断是否为偶数

    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(is_even, numbers))
    print(f"filter() 函数演示:")
    print(f"原始列表: {numbers}")
    print(f"偶数列表: {even_numbers}")
    print()


def exs04():
    """reduce()函数。对序列中的元素进行累积计算"""
    from functools import reduce

    def multiply(x, y):
        return x * y

    numbers = [1, 2, 3, 4, 5]
    product = reduce(multiply, numbers)
    print(f"reduce() 函数演示:")
    print(f"原始列表: {numbers}")
    print(f"所有元素的乘积: {product}")
    print()


def exs05():
    """sorted()函数。自定义排序"""
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78},
        {"name": "Diana", "grade": 95}
    ]

    sorted_by_grade = sorted(students, key=lambda stu: stu["grade"])
    print(f"sorted() 函数演示:")
    print("按成绩升序排序:")
    for student in sorted_by_grade:
        print(f"  {student['name']}: {student['grade']}")

    sorted_by_grade_desc = sorted(students, key=lambda stu: stu["grade"], reverse=True)
    print("\n按成绩降序排序:")
    for student in sorted_by_grade_desc:
        print(f"  {student['name']}: {student['grade']}")
    print()


def exs06():
    """自定义函数"""
    def apply_twice(func, value):
        return func(func(value))

    def add_five(x):
        return x + 5

    result = apply_twice(add_five, 10)
    print(f"自定义高阶函数演示:")
    print(f"对10两次加5的结果: {result}")


def log(func):
    """装饰器是一种特殊的高阶函数，用于动态地增强函数的功能。"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b


print(add(3, 5))    # 输出: 调用函数: add \n 8
