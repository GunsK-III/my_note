import turtle

# 创建画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()

# 绘制正方形
for _ in range(4):
    pen.forward(100)  # 向前移动100像素
    pen.right(90)     # 向右转90度

# 保持窗口打开
screen.mainloop()
