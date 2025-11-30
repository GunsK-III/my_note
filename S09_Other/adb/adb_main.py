from adb_tools import ADBSys
from adb_tools import ADBApp

def test_adb_sys():
    adb1 = ADBSys()
    devices1 = adb1.get_devices()
    # 获取设备列表
    print("---设备列表---\n", devices1, "\n")

    # 获取设备信息
    device_info = adb1.get_device_info(devices1[0]['id'])
    # print("---设备信息---\n", device_info, "\n")

    # 获取设备电量
    battery_level = adb1.get_battery_info(devices1[0]['id'], level_only=True)
    print("---获取电量---\n", battery_level, "\n")

    # 根据关键字搜索包，微信的包名是 com.tencent.mm
    packages = adb1.get_installed_packages(keyword='tencent.mm')
    print("---关键字搜索包---\n", packages, "\n")

    # 重启设备（有二级确认）
    adb1.reboot_device(devices1[0]['id'])

    # 输入文本
    input_str = input("输入要发送的文本，只支持英文：")
    adb1.input_text(input_str)


def test_adb_app():
    adb2 = ADBApp()
    device_id = None  # 如果有设备，可以指定设备ID

    # 1. 点击功能键
    # print("=== 功能键测试 ===")
    # adb2.press_key('back', device_id)  # 按返回键
    # adb2.press_key('home', device_id)  # 按HOME键
    # adb2.press_key('volume_up', device_id)  # 音量加

    # 2. 点击屏幕坐标
    print("\n=== 坐标点击测试 ===")
    adb2.tap_screen(330, 2110, device_id)  # 点击坐标(500, 1000)
    #
    # 3. 滑动屏幕
    print("\n=== 滑动测试 ===")
    # 快速滑动（默认速度）
    adb2.swipe_screen(500, 1500, 500, 500, device_id=device_id)

    # 慢速滑动（持续2秒）
    # adb2.swipe_screen(800, 1000, 200, 1000, duration=2000, device_id=device_id)

    # 带持续时间的滑动
    # adb2.swipe_screen(500, 1500, 500, 500, 1000, device_id)  # 从下往上滑动1秒
