# 字符直角三形	多次循环
def trg1():
    a = str(input("字符:"))
    b = int(input("行数:"))
    for i in range(1, b+1):
        for j in range(i):
            print(a, end="")
        print(end="\n")


def trg2():
    a = str(input("字符："))
    b = int(input("行数："))
    for i in range(1,b+1):
        print(a * i, end="\n")


def trg3():
    str1: str = str(input("字符："))
    int1: int = int(input("行数："))
    for i in range(1, int1 + 1):
        print(" " * (int1 - i), str1 * (2 * i - 1))


if __name__ == '__main__':
    trg3()
    trg2()
    trg1()