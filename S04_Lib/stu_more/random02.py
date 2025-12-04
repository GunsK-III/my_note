# 随机生成验证码

import random
import string

# 生成6位数字验证码
code = ''.join(random.choices('0123456789', k=6))
print(f"验证码：{code}")

# 生成8位混合验证码（字母+数字）
chars = string.ascii_letters + string.digits
code2 = ''.join(random.choices(chars, k=8))
print(f"混合验证码：{code2}")
