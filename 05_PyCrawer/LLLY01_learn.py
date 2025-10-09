"""https://books.toscrape.com/是一个可用于爬虫练习的网站"""
import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}  # 模拟浏览器

res = requests.get('https://books.toscrape.com/')       # 把res变量称为响应体
# print(res)      # 返回Response类的实例，包含HTTP状态码，如果状态码是200，表示请求成功
# print(res.status_code)      # 返回状态码，如果返回404，则表示资源不存在
'''可以用一个条件语句来判断请求是否成功'''
# if res.ok:
#     print('请求成功')
# else:
#     print('请求失败')

print(res.text)       # 网页源码

