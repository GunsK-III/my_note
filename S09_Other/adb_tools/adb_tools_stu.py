import subprocess

class ADBTools:
    def _run_command(self, cmd):
        """执行 ADB 命令并返回输出"""
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None

    def get_devices(self):
        """获取连接的设备列表 5"""
        output = self._run_command(['adb', 'devices'])
        if output:
            lines = output.splitlines()[1:]  # 跳过标题行 “List of devices attached”
            devices = [line.split('\t')[0] for line in lines if line.endswith('device')]
            return devices
        return []

    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_cmd = ['adb'] + (['-s', device_id] if device_id else [])

    def get_battery_info(self):
        """获取电池信息 9"""
        cmd = self.adb_cmd + ['shell', 'dumpsys', 'battery']
        return self._run_command(cmd)

    def get_cpu_info(self):
        """获取 CPU 信息（top 5 进程） 9"""
        cmd = self.adb_cmd + ['shell', 'top', '-n', '1', '-m', '5']
        return self._run_command(cmd)

    def get_installed_packages(self):
        """获取已安装的第三方包列表 26"""
        cmd = self.adb_cmd + ['shell', 'pm', 'list', 'packages', '-3']
        output = self._run_command(cmd)
        if output:
            packages = [line.split(':')[1] for line in output.splitlines()]
            return packages
        return []

    def install_app(self, apk_path):
        """安装 APK"""
        cmd = self.adb_cmd + ['install', apk_path]
        return self._run_command(cmd)

    def uninstall_app(self, package_name):
        """卸载应用"""
        cmd = self.adb_cmd + ['uninstall', package_name]
        return self._run_command(cmd)

    def get_screen_size(self):
        """获取屏幕分辨率 """
        cmd = self.adb_cmd + ['shell', 'wm', 'size']
        output = self._run_command(cmd)
        if output:
            return output.split()[-1]  # 例如 "Physical size: 1080x2340"
        return None
