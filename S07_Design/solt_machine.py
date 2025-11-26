# 老虎机游戏
import random as rd


def solt_machine():
    while True:
        try:
            raw_charge = int(input("请充值积分："))
            break
        except ValueError:
            print("输入值不合法！重新输入！")
    score = raw_charge

    while score < 100:
        while True:
            try:
                raw_charge = int(input(f"当前积分为：{score}。初始积分不可低于100，请再充值积分："))
                break
            except ValueError:
                print("输入值不合法！重新输入！")
        score += raw_charge
    all_raw_charge = raw_charge

    win_1_score = 300
    win_3_score = 1000
    input(f"当前积分有：{score}。每进行一次游戏，消耗100积分。\n"
          f"\033[1;33m键入Enter开始游戏...\033[0m")
    print(f"———————————————————————————————————————")

    num = 0
    while True:
        score -= 100
        num += 1
        solt_list = ['❤️', '💚', '💙', '💛', '🩵', '🤍', '🩷', '💗', '💔']

        object1 = rd.choice(solt_list)
        object2 = rd.choice(solt_list)
        object3 = rd.choice(solt_list)

        print(f"·····({object1}, {object2}, {object3})·····")

        if object1 == object2 and object1 != object3:
            print(f"{object1} × 1，获得奖励：积分+{win_1_score}。")
            score += win_1_score
            print(f"第{num}次进行游戏，当前游戏积分剩余：{score}。")
        elif object1 == object3 and object1 != object2:
            print(f"{object1} × 1，获得奖励：积分+{win_1_score}。")
            score += win_1_score
            print(f"第{num}次进行游戏，当前游戏积分剩余：{score}。")
        elif object2 == object3 and object1 != object3:
            print(f"{object2} × 1，获得奖励：积分+{win_1_score}。")
            score += win_1_score
            print(f"第{num}次进行游戏，当前游戏积分剩余：{score}。")
        elif object1 == object2 and object1 == object3:
            print(f"{object1} × 3，获得奖励：积分+{win_3_score}")
            score += win_3_score
            print(f"第{num}次进行游戏，当前游戏积分剩余：{score}。")
        else:
            print("没有获得任何奖励，积分-100。")
            print(f"第{num}次进行游戏，当前游戏积分剩余：{score}。")
        if object1 == '💗' or object2 == '💗' or object3 == '💗':
            score += 100
            print(f"触发隐藏事件“💗”，积分+100。当前积分剩余：{score}")
        if object1 == '💔' or object2 == '💔' or object3 == '💔':
            score -= 100
            print(f"触发隐藏事件“💔”，积分-100。当前积分剩余：{score}")

        all_charge = all_raw_charge
        while score < 100:
            print(f"\033[1;31m你当前的积分为{score}，"
                  f"剩余积分小于100时无法开始游戏，请再次充值！！！ \033[0m")
            re_charge = int(input("输入充值金额："))
            score += re_charge
            all_charge += re_charge
            if score < 100:
                print(f"充值成功。")
            else:
                print(f"充值成功，当前积分为{score}。"
                      f"\033[1;33m键入Enter继续游戏...\033[0m")

        break_input = input("——————————————————————————————————————")
        if break_input != ' ':
            break
    print(f"\033[1;31m游戏结束，共进行 {num} 轮游戏，累计充值 {all_charge}，当前剩余积分：{score}。\033[0m")
    input("\033[1;33m键入Enter结束程序...\033[0m")


if __name__ == '__main__':
    solt_machine()
