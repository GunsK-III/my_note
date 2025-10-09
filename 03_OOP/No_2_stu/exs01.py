# 开发一个游戏，里面有一个“玩家”角色。这个玩家有名字、生命值、等级、背包等属性，可以执行移动、攻击、拾取物品等操作。

def function1():
    # 使用函数和全局变量（糟糕的设计）
    player_name = ""
    player_health = 100
    player_level = 1
    player_inventory = []

    def init_player(name):
        global player_name, player_health, player_level, player_inventory
        player_name = name
        # ... 初始化其他属性

    def take_damage(amount):
        global player_health
        player_health -= amount

    def add_item(item):
        global player_inventory
        player_inventory.append(item)

    # ... 其他函数


""" 局限：
    1. 全局状态污染：大量全局变量使得代码难以理解和维护。如果游戏中有两个玩家（比如双人游戏），这个设计就完全崩溃了。
    2. 数据与方法分离：玩家的数据（属性）和操作（函数）是割裂的，没有形成一个逻辑整体。
    3. 难以扩展：添加一个新的实体（比如一个“怪物”）需要复制粘贴这套模式，并创建另一套全局变量和函数，极易混淆。"""


def object1():
    # 当需要创建多个拥有相同结构和行为但独立状态的实体时，类是不二之选。
    class Player:
        def __init__(self, name):
            # 状态（属性）在初始化时绑定到每个实例上
            self.name = name
            self.health = 100
            self.level = 1
            self.inventory = []

        # 行为（方法）直接操作自身的数据
        def take_damage(self, amount):
            self.health -= amount

        def add_item(self, item):
            self.inventory.append(item)

        def is_alive(self):
            return self.health > 0

    # 使用：可以轻松创建多个独立的玩家实例
    player1 = Player("Alice")
    player2 = Player("Bob")

    player1.take_damage(20)
    player2.add_item("Sword")

    print(f"{player1.name}'s health: {player1.health}")  # Alice's health: 80
    print(f"{player2.name}'s inventory: {player2.inventory}")  # Bob's inventory: ['Sword']


