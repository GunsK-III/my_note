import requests
from urllib.request import urlopen
# 目标URL
url = 'http://192.168.13.136:8081/api/front/order/cancel'

# 请求头
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# # 遍历ID范围
# for address_id in range(10720, 10758):
#     # 请求体
#     data = {
#         'id': address_id
#     }
#
#     # 发送POST请求
#     response = requests.post(url, headers=headers, data=data)
#
#     # 处理响应
#     if response.status_code == 200:
#         print(f'Successfully deleted address with ID: {address_id}')
#     else:
#         print(f'Failed to delete address with ID: {address_id}, Status Code: {response.status_code}')

rps = urlopen(url)         # 获取响应
print(rps.read().decode('utf-8'))         # 从响应中读取内容
