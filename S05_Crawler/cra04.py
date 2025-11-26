# 删除地址、添加购物车
import requests
import json
from urllib.parse import urlencode


def login_get_token():
    global token
    """
    发送登录请求。
    """
    url = r'http://10.40.92.138:8081/api/front/login'
    payload = {'account': '18292417675',
               'password': 'crmeb@123456'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200 and response.json()['message'] == "操作成功":
        token = response.json()['data']['token']
        # print("获取到了token:", token)
        return token


def address_del():
    url = "http://10.40.92.138:8081/api/front/address/del"
    headers = {
        'authori-zation': login_get_token(),
        "Content-Type": "application/json"
    }
    data = {
        "key1": 122
    }
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data)
    # print(response.status_code)
    print("删除地址", response.text)


def cart_add():
    url = "http://10.40.92.138:8081/api/front/cart/save"
    headers = {
        'authori-zation': login_get_token(),
        "Content-Type": "application/json"
    }
    data = {
        "productId": 8,
        "cartNum": 1,
        "isNew": False,
        "productAttrUnique": 8
    }
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data)
    # print(response.status_code)
    print("添加购物车", response.text)

# cart_add()
address_del()
