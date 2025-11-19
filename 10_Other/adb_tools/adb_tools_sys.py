import subprocess
import platform
from typing import List, Dict, Optional


class ADBSys:
    def __init__(self):
        """初始化ADB工具类，解决中文乱码问题"""
        self.encoding = 'utf-8'
        if platform.system() == 'Windows':
            self.encoding = 'gbk'  # Windows命令行默认使用GBK编码

    def _run_adb_command(self, command: List[str], device_id: str = None) -> tuple:
        """
        执行ADB命令
        Args:
            command: 命令参数列表
            device_id: 设备ID，如果为None则对所有设备执行
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

    def get_devices(self) -> List[Dict[str, str]]:
        """
        查看连接的设备列表
        Returns:
            设备列表，每个设备包含id和status
        """
        success, output = self._run_adb_command(['devices'])
        devices = []

        if success:
            lines = output.split('\n')[1:]  # 跳过第一行标题
            for line in lines:
                if line.strip() and '\t' in line:
                    device_id, status = line.split('\t')
                    devices.append({
                        'id': device_id.strip(),
                        'status': status.strip()
                    })

        return devices

    def reboot_device(self, device_id: str = None) -> bool:
        """
        重启设备（二级确认）
        Args:
            device_id: 设备ID
        Returns:
            是否执行重启
        """
        confirm = input("确定要重启设备吗？(y/N): ")
        if confirm.lower() != 'y':
            print("取消重启")
            return False
        print("设备重启中...")
        success, output = self._run_adb_command(['reboot'], device_id)
        if success:
            print("重启命令已发送，设备正在重启...")
        else:
            print(f"重启失败: {output}")

        return success

    def get_battery_info(self, device_id: str = None, level_only: bool = False) -> Dict:
        """
        获取电池信息
        Args:
            device_id: 设备ID
            level_only: 是否只获取电量百分比
        Returns:
            电池信息字典
        """
        if level_only:
            success, output = self._run_adb_command(['shell', 'dumpsys', 'battery', '|', 'grep', 'level'], device_id)
            battery_info = {}
            if success:
                import re
                match = re.search(r'level:\s*(\d+)', output)
                if match:
                    battery_info['level'] = f"{match.group(1)}%"
            return battery_info
        else:
            success, output = self._run_adb_command(['shell', 'dumpsys', 'battery'], device_id)
            battery_info = {}
            if success:
                for line in output.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        battery_info[key.strip()] = value.strip()
            return battery_info

    def get_cpu_info(self, device_id: str = None) -> Dict:
        """
        获取CPU信息
        Returns:
            CPU信息字典
        """
        cpu_info = {}

        # 获取CPU架构
        success, output = self._run_adb_command(['shell', 'getprop', 'ro.product.cpu.abi'], device_id)
        if success:
            cpu_info['architecture'] = output
        # 获取CPU核心数
        success, output = self._run_adb_command(
            ['shell', 'cat', '/proc/cpuinfo', '|', 'grep', 'processor', '|', 'wc', '-l'], device_id)
        if success:
            cpu_info['cores'] = output.strip()
        # 获取CPU频率
        success, output = self._run_adb_command(
            ['shell', 'cat', '/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq'], device_id)
        if success and output.strip():
            freq_khz = int(output.strip())
            cpu_info['max_frequency'] = f"{freq_khz / 1000:.1f} MHz"

        return cpu_info

    def get_memory_info(self, device_id: str = None) -> Dict:
        """
        获取内存信息
        Returns:
            内存信息字典
        """
        memory_info = {}
        success, output = self._run_adb_command(['shell', 'cat', '/proc/meminfo'], device_id)

        if success:
            for line in output.split('\n'):
                if 'MemTotal:' in line:
                    memory_info['total'] = line.split(':')[1].strip()
                elif 'MemFree:' in line:
                    memory_info['free'] = line.split(':')[1].strip()
                elif 'MemAvailable:' in line:
                    memory_info['available'] = line.split(':')[1].strip()

        return memory_info

    def get_display_info(self, device_id: str = None) -> Dict:
        """
        获取显示系统信息
        Returns:
            显示信息字典
        """
        display_info = {}

        # 获取屏幕分辨率
        success, output = self._run_adb_command(['shell', 'dumpsys', 'display', '|', 'grep', 'mDisplayMode'], device_id)
        if success:
            import re
            match = re.search(r'(\d+) x (\d+)', output)
            if match:
                display_info['resolution'] = f"{match.group(1)}x{match.group(2)}"

        # 获取屏幕密度
        success, output = self._run_adb_command(['shell', 'wm', 'density'], device_id)
        if success:
            import re
            match = re.search(r'Physical density: (\d+)', output)
            if match:
                display_info['density'] = f"{match.group(1)} dpi"

        # 获取屏幕尺寸（物理尺寸较难获取，这里获取一些显示属性）
        success, output = self._run_adb_command(['shell', 'dumpsys', 'window', '|', 'grep', 'mBounds'], device_id)
        if success:
            lines = output.split('\n')
            if lines:
                display_info['display_bounds'] = lines[0].strip()

        return display_info

    def get_device_info(self, device_id: str = None) -> Dict:
        """
        获取完整的设备信息
        Returns:
            包含电池、CPU、内存、显示信息的字典
        """
        return {
            'battery': self.get_battery_info(device_id),
            'cpu': self.get_cpu_info(device_id),
            'memory': self.get_memory_info(device_id),
            'display': self.get_display_info(device_id)
        }

    def get_installed_packages(self, device_id: str = None, system_only: bool = False,
                               third_party_only: bool = False, keyword: str = None) -> List[str]:
        """
        列出安装包
        Args:
            device_id: 设备ID
            system_only: 是否只列出系统包
            third_party_only: 是否只列出第三方包
            keyword: 关键字筛选
        Returns:
            包名列表
        """
        command = ['shell', 'pm', 'list', 'packages']

        if system_only:
            command.append('-s')
        elif third_party_only:
            command.append('-3')

        success, output = self._run_adb_command(command, device_id)
        packages = []

        if success:
            for line in output.split('\n'):
                if line.startswith('package:'):
                    package_name = line.replace('package:', '').strip()
                    if keyword is None or keyword.lower() in package_name.lower():
                        packages.append(package_name)

        return packages

    def input_text(self, text: str, device_id: str = None) -> bool:
        """
        输入文本
        Args:
            text: 要输入的文本
            device_id: 设备ID

        Returns:
            是否执行成功
        """
        # 处理文本中的特殊字符
        text = text.replace(' ', '%s').replace('&', '\\&')
        success, output = self._run_adb_command(['shell', 'input', 'text', text], device_id)

        if success:
            print(f"文本输入成功: {text}")
        else:
            print(f"文本输入失败: {output}")

        return success

