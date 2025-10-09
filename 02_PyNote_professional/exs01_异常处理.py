# try & except 语句 异常处理
# 一定要养成使用 try 进行异常处理的习惯啊，别再一直嵌套 if 啦！
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        """加上ZeroDivisionError关键字后，规定了异常类型，
           即只有发生零除异常时，才会执行except中的代码块"""
        print("division by zero!")
    # except:
    #     """只要发生错误，就执行except，不推荐这样"""
    #     print("an error occurred")
    else:
        print("result is", result)      # 无报错时，会执行else中的代码块
    finally:
        print("executing finally clause")   # 无论是否发生错误，都会执行finally中的代码块


def body():
    try:
        weight = float(input("Enter weight: "))
        height = float(input("Enter height: "))
        bmi = weight / (height ** 2)
    except Exception as e:      # 捕获所有继承自 Exception 的异常（即大多数常见异常），并将异常对象赋值给变量 e。
        print(e)
    else:
        print("BMI:", bmi)


def func_if():
    a = int(input("输入："))
    if a == 0:
        print("a = 0")
    else:
        b = 10 / a
        return b


def func_try():
    try:
        a = int(input("输入："))
        try:
            b = 10 / a
            print(b)
        except ZeroDivisionError:
            print("a是0")
    except ValueError:
        print("a不是数字")
    finally:
        print("程序结束")


func_try()