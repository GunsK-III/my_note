""" CMD命令行交互 """

import subprocess
import sys
import os
from typing import Optional, Union, List, Tuple


class CMD:
    """简单CMD命令执行器"""

    @staticmethod
    def run_cmd(cmd: Union[str, List[str]], timeout: int = 30, cwd: Optional[str] = None,
                encoding: Optional[str] = None) -> Tuple[int, str, str]:
        """
        Desc:
            执行命令并返回结果
        Args:
            cmd: 命令字符串或列表
            timeout: 超时时间（秒）
            cwd: 工作目录
            encoding: 编码，默认自动检测
        Returns:
            返回码, 标准输出, 标准错误
        """
        if encoding is None:
            encoding = 'gbk' if sys.platform == 'win32' else 'utf-8'
        try:
            result = subprocess.run(
                cmd,
                shell=isinstance(cmd, str),
                capture_output=True,
                text=True,
                encoding=encoding,
                errors='ignore',
                timeout=timeout,
                cwd=cwd
            )
            return result.returncode, result.stdout, result.stderr

        except subprocess.TimeoutExpired:
            return -1, "", f"命令执行超时（{timeout}秒）"
        except Exception as e:
            return -1, "", str(e)

    @staticmethod
    def run_cmd_simple(cmd: str, timeout: int = 30) -> str:
        """
        Desc:
            简单执行命令，只返回输出
        Args:
            cmd: 命令字符串
            timeout: 超时时间
        Returns:
            命令输出（成功时）或错误信息（失败时）
        """
        return_code, stdout, stderr = CMD.run_cmd(cmd, timeout)
        return stdout if return_code == 0 else stderr

    @staticmethod
    def run_cmd_check(cmd: str, timeout: int = 30) -> str:
        """
        Desc:
            检查执行命令，失败时抛出异常
        Args:
            cmd: 命令字符串
            timeout: 超时时间
        Returns:
            命令输出
        Raises:
            RuntimeError: 命令执行失败时
        """
        return_code, stdout, stderr = CMD.run_cmd(cmd, timeout)
        if return_code != 0:
            raise RuntimeError(f"命令执行失败（返回码:{return_code}）: {stderr}")
        return stdout

    @staticmethod
    def run_bat(bat_file: str,
                args: Optional[List[str]] = None,
                timeout: int = 60,
                wait: bool = True) -> Tuple[int, str, str]:
        """
        Desc:
            执行BAT脚本（修正版）
        Args:
            bat_file: BAT文件路径（绝对路径或相对路径）
            args: 参数列表
            timeout: 超时时间
            wait: 是否等待BAT执行完成
        Returns:
            (返回码, 标准输出, 标准错误)
        """
        # 转换为绝对路径
        if not os.path.isabs(bat_file):
            bat_file = os.path.abspath(bat_file)
        if not os.path.exists(bat_file):
            return -1, "None", f"BAT文件不存在: {bat_file}"

        cmd_list = ['cmd', '/c']
        if wait:
            cmd_list.append('call')
        cmd_list.append(f'"{bat_file}"')

        # 使用字符串命令确保正确传递路径
        cmd_str = ' '.join(cmd_list)
        # 工作目录设为BAT文件所在目录
        working_dir = os.path.dirname(bat_file)

        return CMD.run_cmd(cmd_str, timeout, cwd=working_dir)

    @staticmethod
    def run_bat_simple(bat_file: str,
                       timeout: int = 60) -> str:
        """
        简单执行BAT脚本，只返回输出
        """
        return_code, stdout, stderr = CMD.run_bat(bat_file, timeout=timeout)
        return stdout if return_code == 0 else stderr
