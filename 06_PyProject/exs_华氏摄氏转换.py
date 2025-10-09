# 华氏度和摄氏度的温度转换
# 摄氏温度（C） = （华氏温度（F） - 32） ÷ 1.8
def F_to_C(temp):
    temp_c = (temp - 32) / 1.8
    print(f"当前摄氏温度为{temp_c:.2f}C，华氏温度为{temp}F")


def C_to_F(temp):
    temp_f = temp * 1.8 + 32
    print(f"当前华氏温度为：{temp_f:.2f}F\n摄氏温度为：{temp}C")


def main():
    temp_input = str(input("输入温度（带单位输入）："))
    temp = float(temp_input[:-1])
    if "F" in temp_input or "f" in temp_input:
        if temp <= -459.67:
            print("输入温度有误。")
        F_to_C(temp)
    elif "C" in temp_input or "c" in temp_input:
        if temp <= -273.15:
            print("输入温度有误。")
        C_to_F(temp)
    else:
        print("输入温度有误。")


if __name__ == "__main__":
    main()


