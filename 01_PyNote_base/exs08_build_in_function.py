""" 内置函数
    目录：
        01. sorted()函数：01 - 04"""


"""1. sorted() 自定义排序函数"""
def exs01():
    """最常用的，可以直接对列表进行排序。"""
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_numbers = sorted(numbers)

    print(sorted_numbers)  # 输出：[1, 2, 5, 5, 6, 9]
    print(numbers)         # 输出：[5, 2, 9, 1, 5, 6] （原列表未被修改）

def exs02():
    """sorted()可以接受任何可迭代对象（如元组、字符串、字典的键等），但返回值始终是一个列表。"""
    # 对元组排序
    my_tuple = (3, 1, 4, 1, 5)
    sorted_tuple = sorted(my_tuple)
    print(sorted_tuple)             # >> [1, 1, 3, 4, 5]

    # 对字符串排序（按字符的 ASCII 码）
    my_string = "python"
    sorted_string = sorted(my_string)
    print(sorted_string)            # >> ['h', 'n', 'o', 'p', 't', 'y']
    # 如果想变回字符串，可以用 join()
    print(''.join(sorted_string))   # >> hnopty

    # 对字典排序（默认对键进行排序）
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    sorted_dict_keys = sorted(my_dict)
    print(sorted_dict_keys)         # >> ['a', 'b', 'c']


def exs03():
    """sorted(iterable, key=function, reverse=False)
       reverse 参数很好理解，就是正序与反序。
       key 参数是自定义排序规则，接受一个函数（通常是简单的 lambda 函数），
       该函数会作用于可迭代对象的每一个元素，然后根据这个函数的返回值进行排序。"""
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]

    sorted_by_grade = sorted(students, key=lambda student: student['grade'])
    print(sorted_by_grade)      # 按成绩升序排序

    sorted_by_grade_desc = sorted(students, key=lambda student: student['grade'], reverse=True)
    print(sorted_by_grade_desc)


def exs04():
    """更复杂的用法，先按成绩降序排序，成绩相同，再按名字升序排序"""
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'David', 'grade': 85},  # 和 Alice 成绩相同
        {'name': 'Charlie', 'grade': 78}
    ]

    # 技巧：key 函数返回一个元组，元组中的元素按优先级排列。
    # 这里，我们希望成绩降序（所以用负数 -grade 来实现），姓名升序。
    sorted_students = sorted(students, key=lambda s: (-s['grade'], s['name']))
    for student in sorted_students:
        print(student)


