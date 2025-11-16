""" 这里研究以一下打印字体的格式化
    详细说明在：https://www.cnblogs.com/wutou/p/17811899.html """

def print_color():
    print("\033[5m这是闪烁的文本\033[0m")
    print("\033[7m这是反显文本\033[0m")
    print("\033[3m这是斜体文本\033[0m")
    print("\033[1;31m这是高亮的红色字体 \033[0m")


if __name__ == '__main__':
    print_color()
