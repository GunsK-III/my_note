from adb_tools_sys import ADBSys
from adb_tools_app import ADBApp

adb = ADBApp()

# 示例用法
devices = []  # 这里可以获取设备列表
device_id = None  # 如果有设备，可以指定设备ID

# 1. 功能键测试
print("=== 功能键测试 ===")
adb.press_key('home', device_id)  # 按HOME键
adb.press_key('back', device_id)  # 按返回键
adb.press_key('volume_up', device_id)  # 音量加

# 2. 坐标点击测试
print("\n=== 坐标点击测试 ===")
adb.tap_screen(500, 1000, device_id)  # 点击坐标(500, 1000)

# 3. 滑动测试
print("\n=== 滑动测试 ===")
# 快速滑动（默认速度）
adb.swipe_screen(500, 1500, 500, 500, device_id=device_id)

# 慢速滑动（持续2秒）
adb.swipe_screen(200, 1000, 800, 1000, duration=2000, device_id=device_id)

# 带持续时间的滑动
adb.swipe_screen(500, 1500, 500, 500, 1000, device_id)  # 从下往上滑动1秒


adb2 = ADBSys()

# 获取设备列表
devices2 = adb2.get_devices()

# 获取第一个设备的完整信息
device_info = adb2.get_device_info(devices[0]['id'])

# 只获取电量
battery_level = adb2.get_battery_info(devices[0]['id'], level_only=True)

# 搜索包含特定关键字的包
packages = adb2.get_installed_packages(keyword='wechat')