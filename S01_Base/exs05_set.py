""" 集合（set）是一个无序的不重复元素序列，支持迭代，可以编辑。
    集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
    目录
        01. 创建集合
        02. 集合运算
        03. 编辑集合
        04. 其它方法、函数"""


def exs01():
    """-创建集合-"""
    set1 = set()            # 创建空集合
    set2: dict = {}         # 这种方法不能创建集合，这是一个空字典
    set3 = {1, 2, 3}
    list1 = [4, 5, 6]
    set4 = set(list1)       # 列表转集合
    str1 = "abcdefg"
    set5 = set(str1)        # 字符串转集合
    print(set1, set2, set3, set4, set5)


def exs02():
    """-集合运算-"""
    set1 = set("abcdef")
    set2 = set("defghi")
    print(set1 & set2)      # 交集运算（& 在python中标识按位与运算，and是逻辑与运算）
    print(set1 | set2)      # 并集运算
    print(set1 - set2)      # 差集运算（set1中包含，set2中不包含）
    print(set1 ^ set2)      # 对称差集运算（不同时包含于set1和set2的元素）


def exs03():
    """-编辑集合-"""
    set1 = set("abcdef")
    set2 = set1.copy()
    # 添加元素
    set1.add("g")                      # 添加一个元素
    print(set1)
    set1.update("h", "i", "j")      # 添加多个字符串元素
    print(set1)
    set1.update([1, 2, 3, "k"])        # 添加多个数字元素
    print(set1)
    set2 |= {"g", "h", "i"}            # 使用并集操作符添加元素
    print(set2)
    # 删除元素
    set3 = set("abcde")
    set3.remove("e")            # 删除元素，元素不存在时会报错
    print("set3:", set3)
    set3.discard("g")           # 删除元素，元素不存在时不会报错
    print("set3:", set3)
    set3.pop()                  # 删除集合中的第一个元素（由于元素的无序的，所以是随机删除的）
    print("set3:", set3)
    set3.clear()                # 删除集合中的所有元素
    print("set3:", set3)


def exs04():
    """-其它方法-"""
    # 计算长度
    set1 = {1, 2, 3, "a", "b", "c", 1, 2}
    print("len(set1):", len(set1))
    # 属于关系
    set2 = {1, 2, 3}
    set3 = {"a"}
    x = 1
    y = "a"
    print("in无法判断包含关系：", set2 in set1, set3 in set1)      # >> False,  False
    print("in可以判断属于关系：", x in set2, y in set2)            # >> True,  True
    # 包含关系
    print("包含关系：", set2.issubset(set1))         # set2 包含于 set1
    print("包含关系：", set1.issuperset(set2))       # set1 包含 set2
