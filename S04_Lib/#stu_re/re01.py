import re


def validate_email(email_str):
    # 定义邮箱的正则表达式
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # 使用 re.match 进行匹配
    if re.match(pattern, email_str):
        return True
    else:
        return False


# 示例输入
email = input("请输入邮箱地址：")
if validate_email(email):
    print("邮箱格式正确！")
else:
    print("邮箱格式不正确，请重新输入！")
