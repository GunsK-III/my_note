""" 列表
    · 列表也属于序列类型的变量
    · 列表可以进行索引、切片、加、乘
    目录
        01.索引、切片
        02.编辑
        03.包含关系、遍历（迭代）
        04.列表函数
        05.列表方法
    """


def exs01():
    """-索引、切片-"""
    list1 = [1, 2, 3, 4, 5]
    print(list1[0], list1[1], list1[-1], list1[-5])     # 索引返回元素。>> 1 2 5 1
    print(list1[0:4])       # 切片返回列表,左闭右开。>> [1, 2, 3, 4]
    print(list1[0:8])       # 切片返回列表。>> [1, 2, 3, 4, 5]
    print(list1[0:-1])      # 左闭右开。>> [1, 2, 3, 4]
    print(list1[:])         # 无参数时默认从开始位置到结束位置。>> [1, 2, 3, 4, 5]
    list2 = ["hello!", "world!"]
    print(list2[0][:-1], list2[1][:-1])      # >> hello world


def exs02():
    """-编辑列表-"""
    # 更新
    list1 = ["一", "二", "三"]
    list1[0] = "四"          # 更新元素
    print(list1, "\n")      # >> ['四', '二', '三']

    # 追加
    list1.append("五")
    print(list1, "\n")      # >> ['四', '二', '三', '五']

    # 插入
    list1.insert(1, "六")
    print(list1, "\n")      # >> ['四', '六', '二', '三', '五']

    # 删除
    list1.remove("六")       # >> 指定元素值，删除第一个匹配项
    print(list1, "\n")      # >> ['四', '二', '三', '五']
    del list1[-1]           # >> 指定索引位置，删除的元素
    print(list1, "\n")      # >> ['四', '二', '三']
    list1.pop(-1)           # 删除指定索引的元素，并返回删除的元素。不填写索引时默认指向最后一个元素。
    print(list1, "\n")      # >> ['四', '二']
    list1.clear()           # 清空列表
    print(list1, "\n")            # >> []

    # 拼接（加运算）（与字符串类似）
    list2, list3 = [1, 2, 3], [4, 5, 6]
    list4 = list2 + list3
    print(list4, "\n")      # >> [1, 2, 3, 4, 5, 6]

    # 乘运算
    list5 = list2 * 2
    print(list5, "\n")      # >> [1, 2, 3, 1, 2, 3]


def exs03():
    """-列表功能-"""
    # 包含关系
    list1, int1 = [1, 2, 3, 4, 5], 2
    int2 = 6
    print(int1 in list1, int2 in list1)     # >> True False

    # 遍历
    for i in list1:
        print(i, end="-")


def exs04():
    """-列表函数-"""
    list1 = [1, 2, 3, 4, 5]
    print(len(list1))       # 列表长度
    print(max(list1))       # >> 5
    print(min(list1))       # >> 1
    tuple1 = tuple(list1)   # 列表转元组
    print(tuple1)
    list2 = list(tuple1)    # 反转
    print(list2)
    str1 = "hello world"
    list3 = list(str1)      # 字符串转列表
    print(list3)
    str2 = "".join(list3)   # 反转
    print(str2)
    set1 = set(list1)       # 列表转集合
    print(set1)             # >> {1, 2, 3, 4, 5}
    list4 = list(set1)      # 反转
    print(list4)


def exs05():
    """-列表方法-"""
    list1 = [1, 2, 3, 4, -2, 0]
    list1.reverse()         # 翻转。返回值None
    print(list1)            # >> [0, -2, 4, 3, 2, 1]
    list1.sort()            # 排序。返回值None
    print(list1)            # >> [-2, 0, 1, 2, 3, 4]
    x = list1.count(2)      # 计数。有返回值
    print(x)                # >> 1
    list2 = list1.copy()    # 复制。有返回值
    print(list2, list1 is list2)    # >> [0, -2, 1, 2, 3, 4] False
