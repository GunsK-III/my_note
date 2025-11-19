import subprocess
import platform
from typing import List, Optional

class ADBApp:
    def __init__(self):
        """初始化ADB输入工具类，解决中文乱码问题"""
        self.encoding = 'utf-8'
        if platform.system() == 'Windows':
            self.encoding = 'gbk'  # Windows命令行默认使用GBK编码

    def _run_adb_command(self, command: List[str], device_id: str = None) -> tuple:
        """
        执行ADB命令
        Args:
            command: 命令参数列表
            device_id: 设备ID
        Returns:
            (success, output) 元组
        """
        try:
            full_cmd = ['adb']
            if device_id:
                full_cmd.extend(['-s', device_id])
            full_cmd.extend(command)
            result = subprocess.run(
                full_cmd,
                capture_output=True,
                text=True,
                encoding=self.encoding,
                timeout=30,
                errors='ignore'
            )

            output = result.stdout.strip() if result.stdout else ""
            error = result.stderr.strip() if result.stderr else ""

            full_output = output
            if error and error not in output:
                full_output = f"{output}\n{error}" if output else error
            return result.returncode == 0, full_output

        except subprocess.TimeoutExpired:
            return False, "命令执行超时"
        except Exception as e:
            return False, f"命令执行错误: {str(e)}"

    def press_key(self, key_type: str, device_id: str = None) -> bool:
        """
        点击功能键
        Args:
            key_type: 按键类型，支持：
                     'power' - 电源键
                     'menu' - 菜单键
                     'home' - HOME键
                     'back' - 返回键
                     'volume_up' - 音量加
                     'volume_down' - 音量减
            device_id: 设备ID

        Returns:
            是否执行成功
        """
        key_mapping = {
            'power': '26',  # KEYCODE_POWER
            'menu': '82',  # KEYCODE_MENU
            'home': '3',  # KEYCODE_HOME
            'back': '4',  # KEYCODE_BACK
            'volume_up': '24',  # KEYCODE_VOLUME_UP
            'volume_down': '25'  # KEYCODE_VOLUME_DOWN
        }

        if key_type not in key_mapping:
            print(f"不支持的按键类型: {key_type}")
            print(f"支持的按键类型: {list(key_mapping.keys())}")
            return False
        keycode = key_mapping[key_type]
        success, output = self._run_adb_command(['shell', 'input', 'keyevent', keycode], device_id)
        if success:
            print(f"{key_type}键按下成功")
        else:
            print(f"{key_type}键按下失败: {output}")

        return success

    def tap_screen(self, x: int, y: int, device_id: str = None) -> bool:
        """
        根据坐标点击屏幕
        Args:
            x: 横坐标
            y: 纵坐标
            device_id: 设备ID
        Returns:
            是否执行成功
        """
        success, output = self._run_adb_command(['shell', 'input', 'tap', str(x), str(y)], device_id)
        if success:
            print(f"点击屏幕坐标 ({x}, {y}) 成功")
        else:
            print(f"点击屏幕坐标 ({x}, {y}) 失败: {output}")
        return success

    def swipe_screen(self, x1: int, y1: int, x2: int, y2: int,
                     duration: Optional[int] = None, device_id: str = None) -> bool:
        """
        根据坐标滑动屏幕
        Args:
            x1: 起始点横坐标
            y1: 起始点纵坐标
            x2: 结束点横坐标
            y2: 结束点纵坐标
            duration: 滑动持续时间（毫秒），如果为None则使用默认速度
            device_id: 设备ID
        Returns:
            是否执行成功
        """
        command = ['shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2)]
        if duration is not None:
            command.append(str(duration))
        success, output = self._run_adb_command(command, device_id)
        if success:
            if duration:
                print(f"从 ({x1}, {y1}) 滑动到 ({x2}, {y2})，持续时间 {duration}ms 成功")
            else:
                print(f"从 ({x1}, {y1}) 滑动到 ({x2}, {y2}) 成功")
        else:
            print(f"滑动失败: {output}")

        return success
