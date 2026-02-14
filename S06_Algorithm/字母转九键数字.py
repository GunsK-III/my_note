# https://www.nowcoder.com/questionTerminal/7960b5038a2142a18e27e4c733855dac
a = input("输入字母数字组合：")
c = 1
e = ""


def zhuan(char, b=""):
    if char in "abc":
        b = "2"
    if char in "def":
        b = "3"
    if char in "ghi":
        b = "4"
    if char in "jkl":
        b = "5"
    if char in "mno":
        b = "6"
    if char in "pqrs":
        b = "7"
    if char in "tuv":
        b = "8"
    if char in "wxyz":
        b = "9"
    return b


for i in a:
    if i.isalpha():
        if i.lower():
            d = zhuan(char=i)
            e += d
        if i.isupper():
            if i == "Z":
                d = "a"
                e += d
            else:
                xiaoXie = i.lower()
                d = chr(ord(xiaoXie) + 1)
                e += d
    if i.isdigit():
        e += i

print(e)
