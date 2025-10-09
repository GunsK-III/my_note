""" 字符串属于可变、序列类型的变量，
    · 此外序列类型还有：列表、元组
    · 序列类型的变量有序、可索引、可切片、可迭代。
    · 可变类型的变量还有：字典、集合
    目录：
        01. 基础
        02. 转义符
        03. 运算符
        04. 格式化
        05. 内建函数
        06. 格式化字符串
        07. f-string """


def exs01():
    """基础"""
    str_a = "hello"  # 字符串定义
    str_b = "world"
    print(len(str_a), len(str_b))  # 字符串长度


def exs02():
    """转义符"""
    print("hello\
    world")                  # 续行符 “\”
    print("hello\nworld")    # 换行符 “\n”
    print("hello\tworld")    # 制表符 “\t”
    print("hello\"world")    # 字符串双引号 “\"”
    print("hello\'world")    # 字符串单引号 “\'”
    print("hello\\world")    # 字符串反斜杠 “\\”
    print("hello\rworld")    # 回车符 “\r”
    print("hello\fworld")    # 换页符 “\f”
    print("hello\bworld")    # 退格符 “\b”
    print("\u0068")          # unicode转义


def exs03():
    """运算符"""
    a = "hello"
    b = "world"
    print(a + b)            # 字符串拼接
    print(a * 3)            # 字符串重复
    print("hel" in a)       # 成员运算符。>>True
    print("hl" not in a)    # 成员运算符。>>Ture
    print(a[0], a[1])       # 索引。>>h e
    print(a[:])             # 截取字符串，左闭右开。>>hello
    print(a[1:])            # >>ello
    print(a[:-1])           # >>hell
    print(a[::-1], a[::2])  # olleh hlo


def exs04():
    """% 占位符"""
    print("0123%s" % "456")     # %s 字符串格式化。>>0123456
    print("0123%d" % 456)       # %d 数值格式化，注意这里是将456插入到%d的位置，所以输出是字符串。>>0123456
    print("0123%f" % 456)       # %f 浮点数格式化，默认6位小数。>>0123456.000000
    print("0123%.2f" % 456)     # %.2f 浮点数格式化，指定2位小数。>>0123456.00
    print("My name is %s and weight is %d kg!" % ('Zara', 21))


def exs05():
    """内建函数"""
    a = "hello World"
    print(a.capitalize())                       # 首字母大写，剩余小写。>>Hello world
    print(a.center(20, "-"))    # 字符串居中，填充字符为-。
    print(a.count("l"))                         # 统计指定字符出现次数。>>3
    print(a.find("l"), a.rfind("c"))            # 找到指定字符的位置，若字符串不存在则返回-1。
    print(a.isalnum())                          # 判断字符串是否只包含数字和字母。>>True
    print("你好hello".isalpha())                 # 判断字符串是否只包含字母。>>True
    print("00123".isdigit())                    # 判断字符串是否只包含数字（0~9）。>>False
    print(a.islower())                          # 判断字符串是否只包含小写字母。>>False
    print(a.isupper())                          # 判断字符串是否只包含大写字母。>>False
    print("一二三".isnumeric())                  # 判断字符串是否只包含数字（Unicode、罗马、中文数字等）。>>True
    print(a.isspace(), "   ".isspace())         # 判断字符串是否只包含空格。>>False  True
    print(a.istitle())                          # 判断字符串是否只包含大写字母。>>False


def exs051():
    """更多内建函数"""
    a, b, c = "", "-", "hello"
    print(a.join(c), b.join(c))     # 将序列中的元素以指定的字符连接生成一个新的字符串
    print(len(c))       # 字符串长度
    print(c.upper())    # 字符串大写
    print(c.upper().lower())    # 字符串小写
    d = " Hi~ "
    print(d.lstrip())   # 去掉字符串左边的空格
    print(d.rstrip())   # 去掉字符串右边的空格
    print(d.strip())    # 去掉字符串左右两边的空格
    print(c.replace("h", "H"))  # 替换字符串
    print(c.swapcase()) # 大小写转换
    print(c.title())    # 标题化
    e = "hello world"
    print(e.split())    # 拆分字符串。>>['hello', 'world']
    print(ord("a"), chr(97))
    print(eval("1+1"))  #字符串转换为表达式。


def exs052():
    """join 用法。str.join(sequence)，将字串作为分隔符插入到序列当中"""
    a = "HelloWorld"
    print("".join(a))       # >>HelloWorld
    print(" ".join(a))      # >>H e l l o W o r l d
    print("-".join(a))      # >>H-e-l-l-o-W-o-r-l-d
    list1 = ["h", "e", "l", "l", "o"]
    print("".join(list1))   # >>Hello
    tuple1 = ("h", "e", "l", "l", "o")
    print("".join(tuple1))  # >>Hello


def exs06():
    """format()格式化字符串"""
    print("{0} {1} {2}".format("a", "b", "c"))      # >>a b c
    print("{1} {0} {2}".format("a", "b", "c"))      # >>b a c
    print("我叫{name}，我是{career}".format(name="小王", career="程序员"))        # >>我叫小王，我是程序员


def exs07():
    """f-string"""
    name, career = "小王", "程序员"                  # 可以单独定义
    print(f"我叫{name}，我是{career}")

    dicti = {"name": "小王", "career": "程序员"}     # 也可以使用字典
    print(f"我叫{dicti['name']}，我是{dicti['career']}")
