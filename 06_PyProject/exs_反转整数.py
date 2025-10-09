# 反转整数
x = int(input("输入数字："))
if x >= 0:
    str_x = str(x)
    rev_str_x = str_x[::-1]
    rev_x = int(rev_str_x)
    print(rev_x)
else:
    abs_x = abs(x)
    str_x = str(abs_x)
    rev_str_x = str_x[::-1]
    rev_x = int(rev_str_x)
    real_rev_x = rev_x * (-1)
    print(real_rev_x)
