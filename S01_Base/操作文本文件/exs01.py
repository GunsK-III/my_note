"""文件操作"""
def read1():
    """读取文件（基础）"""
    f = open(r"file01.txt", "r", encoding="utf-8")
    print(f.read())     # 输出文件内容
    print(f.read())     # 输出空，因为这个方法会从当前文件指针位置开始读，此时指针已经到最后了
    print(f.tell())     # 获取当前文件指针位置
    f.seek(0)           # 移动文件指针位置到开头
    print(f.read())     # 输出文件内容
    f.close()

    f = open(r"file01.txt", "r", encoding="utf-8")
    print(f.read(10))     # 从指针位置开始，读取10个字节内容
    print(f.read(20))
    f.close()


def read2():
    """ 读取文件（按行读取）"""
    f = open("file01.txt", "r", encoding="utf-8")
    print(f.readline())         # 从指针位置开始读取一行内容
    print(f.readline(), end="\n")
    f.close()

    f = open("file01.txt", "r", encoding="utf-8")
    for line in f:
        print(line)             # 逐行输出
    f.close()

    f = open("file01.txt", "r", encoding="utf-8")
    print(f.readlines())        # 返回一个列表，列表中的元素是每行内容。依然从指针位置开始
    f.close()


def read3():
    """with提供了一种优雅的方式来处理文件操作、数据库连接等需要明确释放资源的场景。"""
    with open(r"../02_PyNote_professional/_file01.txt", "r", encoding="utf-8") as f:
        print(f.read())      # 在这内容执行完毕后，文件自动关闭


def write1():
    with open("file02.txt", "w", encoding="utf-8") as f:
        # w模式，若文件不存在，则创建文件，若文件存在，则清空文件内容
        f.write("hello,")
        f.write("world!\n")
        f.write("ohhhh!")
        # f.read()        # 不支持读操作。>> io.UnsupportedOperation: not readable


def write2():
    with open("file03.txt", "a", encoding="utf-8") as f:
        # 追加模式，若文件不存在，则创建文件，若文件存在，则可以追加内容
        f.write("hello,world! ")
        # f.read()        # 不支持读操作。>> io.UnsupportedOperation: not readable


def write3():
    with open("file02.txt", "r+", encoding="utf-8") as f:
        # r+模式，读写文件，指针默认位置位于文件开头，写入内容会覆盖掉原来内容。文件不存在，则报错
        f.write("11111")    # 写入内容，并将指针移动至插入内容的后面。
        print(f.read())     # 此时，输出指针之后的内容。


def write4():
    """
    seek(offset, whence=0)方法用于移动文件指针到指定位置，改变下一次读写操作的起始位置。
    offset: 偏移量，单位为字节（一个英文/数字字符是1字节，一个汉字字符是3字节）
    whence: 参考位置，默认为0
    0 - 文件开头（默认值）
    1 - 当前位置
    2 - 文件末尾
    注意：在文本模式下，Python不支持相对于当前位置或文件末尾的非零偏移量的seek操作。
    文本模式需要处理字符编码，而不同编码的字符长度不同，因此Python进行限制，以避免定位到字符的中间位置导致解码错误。
    """
    with open("file02.txt", "r+b") as f:
        f.seek(5)            # 移动指针到开头第5个字节处
        f.seek(1, 1)         # 移动指针从当前位置向后移动5个字节处
        f.seek(-5, 2)        # 移动指针从文件末尾向前移动5个字节处
        f.seek(0, 2)         # 移动指针到文件末尾
        print(f.read())      # 二进制模式下，输出：b''，内容在引号中

    with open("file02.txt", "r+", encoding="utf-8") as f:
        # 文本模式下，seek()方法只能使用绝对位置进行定位，不能使用当前位置。
        f.seek(5)
        f.seek(0)
        f.seek(0, 2)


def write5():
    with open("file04.txt", "a+", encoding="utf-8") as f:
        # a+模式，读写文件，指针默认位置位于文件末尾，写入内容会追加到文件末尾。文件不存在，则创建文件。
        print("写入之前：", f.read())
        f.write("11111")
        f.seek(0)
        print("写入之后：", f.read())


def file1():
    with open("file05.txt", "a+", encoding="utf-8") as f:
        print("文件名称：", f.name)
        print("当前指针的位置：", f.tell())


