""" 计算器
    可进行加（+）、减（-）、乘（*、×）、除（/、÷）、幂（**）、开跟（√）、对数（log）
    2024/05/03
"""

import math
from decimal import Decimal


def calculator():
    num_1 = float(input("input 1st number:"))
    num_2 = float(input("input 2sd number:"))
    str1, str2 = str(num_1), str(num_2)
    sign = input("input operator:")
    if sign == "+":
        return Decimal(str1) + Decimal(str2)
    elif sign == "-":
        if (num_1 - num_2) % 1 == 0:
            return int(num_1 - num_2)
        else:
            return Decimal(str1) - Decimal(str2)
    elif sign == "*" or sign == "×":
        prd = Decimal(str1) * Decimal(str2)
        if prd % 1 == 0:
            return int(prd)
        else:
            return prd
    elif sign == "/" or sign == "÷":
        if num_2 == 0:
            return "error"
        else:
            quo = num_1 / num_2
            if quo % 1 == 0:
                return int(quo)
            else:
                return round(quo, 3)
    elif sign == "**":
        mi = num_1 ** num_2
        if mi % 1 == 0:
            return int(mi)
        else:
            return round(mi, 3)
    elif sign == "√":
        if num_2 == 0:
            return "error"
        else:
            return num_1 ** (1 / num_2)
    elif sign == "log":
        if num_1 == 0 or num_2 == 0:
            return "error"
        else:
            res = math.log(num_2, num_1)  # (指数, 底数)
            if res % 1 == 0:
                return int(res)
            else:
                return round(res, 3)


while True:
    try:
        print("result:", calculator())
        if input("键入q退出\n继续请按任意键...") == 'q':
            break
    except KeyboardInterrupt:
        print("\n进程已被终止")
        break
