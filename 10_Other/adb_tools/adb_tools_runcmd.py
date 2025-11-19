import subprocess
import platform
from typing import List, Optional

encoding = 'utf-8'
if platform.system() == 'Windows':
    encoding = 'gbk'

def run_adb_command(command: List[str], device_id: str = None) -> tuple:
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
            encoding=encoding,
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
