""" 字典是另一种可变容器模型，且可存储任意类型对象。"""


def exs01():
    """-基本信息-"""
    dict1 = {}  # 定义空字典
    print(dict1)
    dict2 = {"name": "张三", "age": 18, "sex": "男"}
    print(dict2)
    # print(dict2[0])                   # 字典无索引>> KeyError: 0
    print(dict2["name"])
    print("length:", len(dict2))        # 查看字典数量
    str1 = str(dict2)                   # 字典转字符串
    print("str1:", str1, type(str1))    # >> dict2


def exs02():
    """-编辑-"""
    """修改字典中的值"""
    dict1 = {"name": "张三", "age": 18, "sex": "男"}
    print(dict1)
    dict1["name"] = "李四"  # 修改字典中的值
    print(dict1)

    """添加"""
    dict1["city"] = "上海"  # 添加
    print(dict1)

    """删除"""
    del dict1["city"]  # 删除键
    print(dict1)
    dict1.clear()  # 清空字典
    print(dict1)
    del dict1  # 删除字典
    # print(dict1)          # >> UnboundLocalError

    """两个字典合并"""
    dict2 = {"a": "A", "b": "B", "c": "C"}
    dict3 = {"d": "D", "e": "E", "f": "F"}
    dict4 = dict(dict2, **dict3)        # 合并字典
    print("dict4", dict4)
    dict5 = {**dict2, **dict3}          # 合并
    print("dict5", dict5)
    dict6 = dict2 | dict3               # 合并
    print("dict6", dict6)
    dict2.update(dict3)                 # 合并，将dict3的值覆盖到dict2的键
    print("dict2", dict2)


def exs03():
    """字典的特性"""
    dict1 = {"a": "A", "b": "B", "c": "C", "a": "AA"}  # 如果有重复的键，则取最后一个值
    print(dict1)
    """遍历"""
    for key in dict1:             # 默认遍历字典中的键
        print(key, end=" ")

    print("")
    for key in dict1.keys():     # 遍历字典中的键
        print(key, end=" ")

    print("")
    for value in dict1.values():  # 遍历字典中的值
        print(value, end=" ")

    """键必须不可变，所以可以用数字，字符串或元组充当，而用列表、集合就不行，"""
    # dict2 = {(1, 2): "A", [3, 4]: "B", {5, 6}: "C"}
    # print(dict2)                # >> TypeError


def exs04():
    """试图（方法） """
    dict1 = {"name": "张三", "age": 18, "sex": "男"}
    print(dict1.values(), dict1.keys())
    print(dict1.items())
    for i, j in dict1.items():
        print(i, ":\t", j)




