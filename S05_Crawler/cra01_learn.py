from urllib.request import urlopen

url = 'http://www.baidu.com'        # 打开一个网址
rps = urlopen(url)         # 获取响应
print(rps.read().decode('utf-8'))         # 从响应中读取内容

