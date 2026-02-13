# 基于本地数据库模拟存钱和取钱
import sqlite3
import re


class BankAccount:
    def __init__(self):      # 创建数据库连接和游标
        self.conn = sqlite3.connect("PyFile/bank.db")
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):            # 创建账户表
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS account (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                balance REAL NOT NULL CHECK(balance >= 0)
            )
        ''')
        # 初始化账户余额（如果不存在）
        self.cursor.execute("SELECT COUNT(*) FROM account")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO account (balance) VALUES (0.00)")
            self.conn.commit()

    def deposit(self, amount):
        amount = round(float(amount), 2)
        self.cursor.execute("UPDATE account SET balance = balance + ? WHERE id = 1", (amount,))
        self.conn.commit()
        print(f"存款成功，当前余额为: {self.get_balance():.2f}")

    def withdraw(self, amount):
        amount = round(float(amount), 2)
        self.cursor.execute("SELECT balance FROM account WHERE id = 1")
        current_balance = self.cursor.fetchone()[0]
        if current_balance < amount:
            print("余额不足，无法取款")
            return
        self.cursor.execute("UPDATE account SET balance = balance - ? WHERE id = 1", (amount,))
        self.conn.commit()
        print(f"取款成功，当前余额为: {self.get_balance():.2f}")

    def get_balance(self):
        self.cursor.execute("SELECT balance FROM account WHERE id = 1")
        return self.cursor.fetchone()[0]

    def valid_amount(self, input_str):
        """验证金额是否为正数，且小数点后最多两位"""
        pattern = r'^\d+(\.\d{1,2})?$'
        return re.fullmatch(pattern, input_str)

    def run(self):
        while True:
            print("\n当前余额为: {:.2f}".format(self.get_balance()))
            choice = input("请选择操作:\n1. 存钱\n2. 取钱\n其他任意键退出\n请输入选项: ")
            if choice == '1':
                amount_input = input("请输入存钱金额: ")
                if not self.valid_amount(amount_input):
                    print("输入无效，请输入正数且小数点后最多两位。")
                    continue
                self.deposit(amount_input)
            elif choice == '2':
                amount_input = input("请输入取钱金额: ")
                if not self.valid_amount(amount_input):
                    print("输入无效，请输入正数且小数点后最多两位。")
                    continue
                self.withdraw(amount_input)
            else:
                print("退出程序。")
                break


# 运行程序
if __name__ == "__main__":
    account = BankAccount()
    account.run()
