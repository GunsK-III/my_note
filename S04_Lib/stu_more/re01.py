"""         正则表达式（Regular Expression）
元字符	    说明	                                示例
 .	      匹配任意单个字符（除换行符）	            a.c     →  abc、aXc
 \d	      匹配数字（等价于 [0-9]）	                \d\d    →  42、99
 \w	      匹配单词字符（字母、数字、下划线）	        \w+     →  hello、a1_
 \s       匹配空白字符（包括空格、制表符、换行符）      \s+     →  hello world
 +	      匹配前一个字符 1 次或多次	                a+      →  a、aa、aaa
 *	      匹配前一个字符 0 次或多次	                ab*c    →  ac、abc、abbc
 ?	      匹配前一个字符 0 次或 1 次	            ab?c    →  ac、abc
 ^	      匹配字符串开头	                        ^Hello  →  Hello world（匹配开头）
 $	      匹配字符串结尾	                        world$  →  Hello world（匹配结尾）
 [ ]	  匹配括号内的任意一个字符	                [aeiou] →  匹配所有元音字母
 `	      `	                                    或（匹配左侧或右侧）
 ()	      分组（用于提取或重复）	                (ab)+   →  ab、abab

"""

import re

def exs01():
    """
    re.match(pattern, string)
    从字符串开头开始匹配，如果开头不匹配就返回 None。
    """
    print(re.match('www', 'www.baidu.com').span())  # 匹配部分在原字符串中的位置范围
    print(bool(re.match('www', 'www.baidu.com')))   # >> True
    print(bool(re.match('com', 'www.baidu.com')))   # >> False
    print(re.match(r'\d+', '123abc').group())       # 获取匹配到的内容并打印


def exs02():
    """
    re.search(pattern, string)
    在整个字符串中搜索第一个匹配项，找到就返回，否则返回 None。
    """
    print(re.search(r'\d+', 'abc123def').group())   # >> 123
    print(re.search(r'\w+', 'abc123def').group())   # >> abc123def
    print(re.search(r'\d+', 'abcdef'))              # >> None


def exs03():
    """
    re.findall(pattern, string)
    返回所有非重叠匹配结果的列表（没有匹配则返回空列表）。
    """
    text = "电话: 13800138000, 备用: 13900139000"
    phones = re.findall(r'\d{11}', text)
    print(phones)  # >> ['13800138000', '13900139000']


def exs04():
    """
    re.sub(pattern, repl, string)
    将字符串中所有匹配 pattern 的部分替换为 repl。
    """
    text = "今天是2025年1月1日"
    new_text = re.sub(r'\d+', 'X', text)
    print(new_text)  # >> 今天是X年X月X日


def exs05():
    """
    re.split(pattern, string)
    按正则表达式分割字符串。
    """
    parts = re.split(r'\s+', 'apple  banana\torange\ngrape')
    print(parts)  # >> ['apple', 'banana', 'orange', 'grape']


def exs06():
    """ 示例 """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    text = "联系我：user@example.com 或 admin@test.org"
    emails = re.findall(email_pattern, text)
    print(emails)  # >> ['user@example.com', 'admin@test.org']


# 验证邮箱格式
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# 提取网页中的所有链接
def extract_links(html):
    pattern = r'href="(https?://[^"]+)"'
    return re.findall(pattern, html)

# 清理文本中的多余空格
def clean_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()


# 使用编译提高性能（多次使用同一模式时）
pattern = re.compile(r'\d+')
numbers = pattern.findall("我有3个苹果和15个橘子")  # >> ['3', '15']
