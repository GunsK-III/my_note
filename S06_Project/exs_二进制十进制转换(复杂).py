# 将输入的二进制数转换为十进制数输出
def bin_to_dec():
    binary = input("输入一个二进制数：").strip()

    # 处理负数
    is_negative = binary.startswith('-')
    if is_negative:
        binary = binary[1:]

    # 处理小数点
    if '.' in binary:
        integer_part, decimal_part = binary.split('.')
    else:
        integer_part, decimal_part = binary, ''

    # 转换整数部分
    decimal = 0
    for i in range(len(integer_part)):
        decimal += int(integer_part[i]) * 2 ** (len(integer_part) - i - 1)

    # 转换小数部分
    for i in range(len(decimal_part)):
        decimal += int(decimal_part[i]) * 2 ** -(i + 1)

    if is_negative:
        decimal = -decimal

    print(f"{binary if not is_negative else '-' + binary}的十进制数是：{decimal}")
    input("输入enter继续")


def dec_to_bin():
    decimal_str = input("输入一个十进制数：").strip()

    # 处理负数
    is_negative = decimal_str.startswith('-')
    if is_negative:
        decimal_str = decimal_str[1:]

    # 处理小数点
    if '.' in decimal_str:
        integer_part, decimal_part = decimal_str.split('.')
        integer_part = int(integer_part)
        decimal_part = float('0.' + decimal_part)
    else:
        integer_part = int(decimal_str)
        decimal_part = 0.0

    # 转换整数部分
    if integer_part == 0:
        binary_integer = '0'
    else:
        binary_integer = ""
        temp = integer_part
        while temp > 0:
            binary_integer = str(temp % 2) + binary_integer
            temp = temp // 2

    # 转换小数部分
    binary_decimal = ""
    if decimal_part > 0:
        binary_decimal = "."
        count = 0
        while decimal_part > 0 and count < 10:  # 限制小数点后10位
            decimal_part *= 2
            bit = int(decimal_part)
            binary_decimal += str(bit)
            decimal_part -= bit
            count += 1

    result = binary_integer + binary_decimal
    if is_negative:
        result = '-' + result

    print(f"{decimal_str if not is_negative else '-' + decimal_str}的二进制数是：{result}")
    input("输入enter继续")


if __name__ == '__main__':
    while True:
        print("1.二进制转十进制\n"
              "2.十进制转二进制\n"
              "3.退出")
        try:
            choice = int(input("请输入你的选择："))
            if choice == 1:
                bin_to_dec()
            elif choice == 2:
                dec_to_bin()
            elif choice == 3:
                break
            else:
                print("输入错误，请重新输入")
        except ValueError:
            print("输入格式错误，请输入数字")

