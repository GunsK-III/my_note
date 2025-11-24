# 推导式（Comprehensions）是一种快速创建列表、集合、字典甚至生成器的方式


def exs01():
    """ 1. 列表推导式
           语法：[表达式 for 变量 in 可迭代对象 if 条件]
    """
    # 创建一个包含 0 到 9 的平方的列表
    squares = [x ** 2 for x in range(10)]
    print(squares)          # >> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 只保留偶数的平方
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(even_squares)     # >> [0, 4, 16, 36, 64]


def exs02():
    """ 2. 集合推导式
           语法：{表达式 for 变量 in 可迭代对象 if 条件}
    """
    # 去重并平方
    unique_squares = {x ** 2 for x in [1, 2, 2, 3, 4, 4]}
    print(unique_squares)   # >> {1, 4, 9, 16}


def exs03():
    """ 3. 字典推导式
        语法：{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
    """
    # 将列表中的元素作为键，其平方作为值
    numbers = [1, 2, 3, 4]
    square_dict = {x: x ** 2 for x in numbers}
    print(square_dict)      # >> {1: 1, 2: 4, 3: 9, 4: 16}

    # 反转字典
    original = {'a': 1, 'b': 2, 'c': 3}
    reversed_dict = {v: k for k, v in original.items()}
    print(reversed_dict)    # >> {1: 'a', 2: 'b', 3: 'c'}

