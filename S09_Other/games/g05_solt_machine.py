import random
import time
import os


class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣", "💎", "🍀", "💖"]
        self.payouts = {
            ("🍒", "🍒", "🍒"): 10,
            ("🍋", "🍋", "🍋"): 15,
            ("🔔", "🔔", "🔔"): 20,
            ("⭐", "⭐", "⭐"): 25,
            ("7️⃣", "7️⃣", "7️⃣"): 50,
            ("💎", "💎", "💎"): 100,
            ("🍀", "🍀", "🍀"): 75,
            ("💖", "💖", "💖"): 60,
        }
        self.balance = 100  # 初始余额
        self.min_bet = 5
        self.max_bet = 50

    def clear_screen(self):
        """清空命令行屏幕"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def spin_wheels(self):
        """转动转轮，返回三个随机符号"""
        return [random.choice(self.symbols) for _ in range(3)]

    def calculate_payout(self, wheels, bet):
        """计算奖金"""
        # 检查是否三个相同
        if wheels[0] == wheels[1] == wheels[2]:
            symbol = wheels[0]
            for combo, multiplier in self.payouts.items():
                if combo[0] == symbol:
                    return bet * multiplier

        # 检查是否有两个相同
        elif wheels[0] == wheels[1] or wheels[1] == wheels[2] or wheels[0] == wheels[2]:
            return bet * 2

        # 没有匹配
        return 0

    def display_wheels(self, wheels, final=False):
        """显示转轮"""
        if final:
            print("=" * 30)
            print("     最终结果:")
            print("    ┌─────┬─────┬─────┐")
            print(f"    │ {wheels[0]}  │  {wheels[1]} │  {wheels[2]}│")
            print("    └─────┴─────┴─────┘")
            print("=" * 30)
        else:
            print("    ┌─────┬─────┬─────┐")
            print(f"    │ {wheels[0]}  │ {wheels[1]}  │ {wheels[2]} │")
            print("    └─────┴─────┴─────┘")

    def animate_spin(self):
        """显示转轮动画"""
        print("\n转轮转动中...")
        for _ in range(10):
            temp_wheels = [random.choice(self.symbols) for _ in range(3)]
            self.display_wheels(temp_wheels)
            time.sleep(0.1)
            self.clear_screen()
            print("=== 老虎机游戏 ===")
            print(f"当前余额: ${self.balance}")

    def get_bet(self):
        """获取玩家下注金额"""
        while True:
            try:
                print(f"\n最小下注: ${self.min_bet}, 最大下注: ${self.max_bet}")
                bet = int(input(f"请输入下注金额 (当前余额: ${self.balance}): $"))

                if bet < self.min_bet:
                    print(f"下注金额不能小于 ${self.min_bet}!")
                elif bet > self.max_bet:
                    print(f"下注金额不能大于 ${self.max_bet}!")
                elif bet > self.balance:
                    print("余额不足!")
                else:
                    return bet
            except ValueError:
                print("请输入有效的数字!")

    def show_payout_table(self):
        """显示赔率表"""
        print("\n" + "=" * 40)
        print("              赔率表")
        print("=" * 40)
        for combo, multiplier in self.payouts.items():
            print(f"  {combo[0]} {combo[1]} {combo[2]} : {multiplier}倍")
        print("-" * 40)
        print("  任意两个相同符号: 2倍")
        print("=" * 40)

    def play(self):
        """主游戏循环"""
        self.clear_screen()
        print("=== 欢迎来到老虎机游戏! ===")
        print(f"初始余额: ${self.balance}")

        while self.balance > 0:
            print("\n选项:")
            print("1. 开始游戏")
            print("2. 查看赔率表")
            print("3. 退出游戏")

            choice = input("请选择 (1-3): ")

            if choice == "1":
                # 获取下注金额
                bet = self.get_bet()
                self.balance -= bet

                # 显示动画
                self.clear_screen()
                print("=== 老虎机游戏 ===")
                print(f"当前余额: ${self.balance}")
                print(f"下注金额: ${bet}")

                self.animate_spin()

                # 获取最终结果
                final_wheels = self.spin_wheels()
                self.clear_screen()
                print("=== 老虎机游戏 ===")
                print(f"当前余额: ${self.balance}")
                print(f"下注金额: ${bet}")

                self.display_wheels(final_wheels, final=True)

                # 计算奖金
                payout = self.calculate_payout(final_wheels, bet)

                if payout > 0:
                    print(f"\n恭喜! 你赢得了 ${payout}!")
                    self.balance += payout
                else:
                    print("\n很遗憾，没有中奖。")

                print(f"当前余额: ${self.balance}")

                # 检查是否破产
                if self.balance < self.min_bet:
                    print(f"\n你的余额不足 ${self.min_bet}，无法继续游戏。")
                    print("游戏结束!")
                    break

                input("\n按Enter键继续...")
                self.clear_screen()

            elif choice == "2":
                self.clear_screen()
                print("=== 老虎机游戏 ===")
                self.show_payout_table()
                input("\n按Enter键返回主菜单...")
                self.clear_screen()

            elif choice == "3":
                print(f"\n游戏结束! 最终余额: ${self.balance}")
                if self.balance > 100:
                    print(f"你赚了 ${self.balance - 100}!")
                elif self.balance < 100:
                    print(f"你损失了 ${100 - self.balance}!")
                else:
                    print("不赚不赔!")
                break
            else:
                print("无效选择，请重新输入!")

        if self.balance <= 0:
            print("\n你的余额已用完!")
            print("游戏结束!")


if __name__ == "__main__":
    game = SlotMachine()
    game.play()
