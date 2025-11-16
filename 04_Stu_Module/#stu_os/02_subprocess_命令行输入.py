import os
import subprocess

def exs01():
    os.system('chcp 65001')     # Change Code Page，65001 代表 UTF-8 编码页。
    os.system('ipconfig')

# 调用上面的函数，会发现即便执行了 chcp 65001 命令，可是控制台中还是有乱码中文件，
# 所以执行复杂CMD命令时，建议使用 subprocess 模块。
# subprocess 是 Python 标准库中用于创建和管理子进程的模块，
# 允许在 Python 程序中执行外部命令，并与这些命令进行交互。

def exs02():
    result = subprocess.run("ipconfig", shell=True, capture_output=True, encoding='gbk')
    print(result.stdout)

def exs03():        # 执行多行命令也不再话下
    command = """
        curl ^"https://chat.deepseek.com/api/v0/chat/message_feedback^" ^
        -H ^"accept: */*^" ^
        -H ^"accept-language: zh-CN,zh;q=0.9,en;q=0.8^" ^
        -H ^"authorization: Bearer 5wuDsqPtDKSFECprNTdwQMX3OxkIUkgfbM9PWh2QJ1EsISMGhaEDK/QLhHPW/906^" ^
        -H ^"content-type: application/json^" ^
        -b ^"intercom-device-id-guh50jw4=1930be8b-6875-4e85-a461-2fc81ca90292; HWWAFSESID=2335b586622ba11eceb; HWWAFSESTIME=1763292216452; ds_session_id=3b282e834fdd4275bdd8cc28b81f1e36; intercom-session-guh50jw4=VGtwb0xzWlBPWHRVRldMZXZaSy9YK010UVdvQTEvdE5xTnBYTXFCNHZZdFMxbW85bExINDRZWkpzMmxnc29jcnNTRjlVaUxiNkI2T2JQcDdhV2o5SytFQm1idVBjaFBkT1ZOenArMitvUEE9LS1ySG5hSFhla0NtbCtNbDU3YXFDUGxBPT0=--4dc87937901fe112fb4293442fb60aa2011ef6b0^" ^
        -H ^"origin: https://chat.deepseek.com^" ^
        -H ^"priority: u=1, i^" ^
        -H ^"referer: https://chat.deepseek.com/a/chat/s/cc20e94b-9da7-4274-95c5-719993b10081^" ^
        -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"142^\^", ^\^"Microsoft Edge^\^";v=^\^"142^\^", ^\^"Not_A Brand^\^";v=^\^"99^\^"^" ^
        -H ^"sec-ch-ua-mobile: ?0^" ^
        -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
        -H ^"sec-fetch-dest: empty^" ^
        -H ^"sec-fetch-mode: cors^" ^
        -H ^"sec-fetch-site: same-origin^" ^
        -H ^"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0^" ^
        -H ^"x-app-version: 20241129.1^" ^
        -H ^"x-client-locale: zh_CN^" ^
        -H ^"x-client-platform: web^" ^
        -H ^"x-client-version: 1.5.0^" ^
        -H ^"x-debug-lite-model-channel: prod^" ^
        -H ^"x-debug-model-channel: prod^" ^
        --data-raw ^"^{^\^"chat_session_id^\^":^\^"cc20e94b-9da7-4274-95c5-719993b10081^\^",^\^"message_id^\^":8,^\^"feedback_type^\^":^\^"GOOD^\^"^}^"
    """
    result = subprocess.run(command, shell=True, capture_output=True, encoding='gbk')
    print("已执行。\n", result)

