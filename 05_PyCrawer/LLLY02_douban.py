# 爬取豆瓣电影Top250网页页面（https://movie.douban.com/top250）
import requests
# res = requests.get('https://movie.douban.com/top250')
# print(res.status_code)      # >>418，这并不是一个成功的状态码，4开头的状态码表示客户端错误
# print(res.text)           # 返回空
'''要查看具体的状态码含义，访问：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status'''
'''可以通过定义请求头的方法，绕过豆瓣的对爬虫的拦截。下面让我再来试一遍'''

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}
res = requests.get('https://movie.douban.com/top250', headers=headers)
print(res.status_code)      # >>200，^_^ok
print(res.text)


