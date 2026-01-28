"""         正则表达式（Regular Expression）
元字符	    说明	                            示例
 .	      匹配任意单个字符（除换行符）	        a.c    →  abc、aXc
 \d	      匹配数字（等价于 [0-9]）	            \d\d   →  42、99
 \w	      匹配单词字符（字母、数字、下划线）	    \w+    →  hello、a1_
 +	      匹配前一个字符 1 次或多次	            a+     →  a、aa、aaa
 *	      匹配前一个字符 0 次或多次	            ab*c   →  ac、abc、abbc
 ?	      匹配前一个字符 0 次或 1 次	        ab?c   →  ac、abc
 ^	      匹配字符串开头	                    ^Hello →  Hello world（匹配开头）
 $	      匹配字符串结尾	                    world$ →  Hello world（匹配结尾）
 [ ]	  匹配括号内的任意一个字符	            [aeiou] → 匹配所有元音字母
 `	      `	                                或（匹配左侧或右侧）
 ()	      分组（用于提取或重复）	            (ab)+  → ab、abab

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
