import os
import sys
import logging
import logging.handlers
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


class Logger:
    """自定义日志记录器"""
    def __init__(self,
                 name: str = 'app',
                 log_dir: Optional[Union[str, Path]] = None,
                 log_level: str = 'INFO',
                 console_output: bool = True,
                 file_output: bool = True,
                 max_file_size: int = 10 * 1024 * 1024,  # 10MB
                 backup_count: int = 5):
        """
        初始化日志记录器
        Args:
            name: 日志记录器名称
            log_dir: 日志文件目录，默认当前目录下的logs文件夹
            log_level: 日志级别
            console_output: 是否输出到控制台
            file_output: 是否输出到文件
            max_file_size: 单个日志文件最大大小（字节）
            backup_count: 备份文件数量
        """
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LOG_LEVELS.get(log_level.upper(), logging.INFO))

        # 避免重复添加handler
        if self.logger.handlers:
            self.logger.handlers.clear()

        # 设置日志格式
        self._setup_formatter()

        # 控制台输出
        if console_output:
            self._add_console_handler()

        # 文件输出
        if file_output:
            self._add_file_handler(log_dir, max_file_size, backup_count)

    def _setup_formatter(self):
        """设置日志格式"""
        self.formatter = logging.Formatter(
            fmt='%(asctime)s.%(msecs)03d %(levelname)s %(message)s',
            datefmt='%Y.%m.%d %H:%M:%S'
        )

    def _add_console_handler(self):
        """添加控制台处理器"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(console_handler)

    def _add_file_handler(self,
                          log_dir: Optional[Union[str, Path]] = None,
                          max_file_size: int = 10 * 1024 * 1024,
                          backup_count: int = 5):
        """添加文件处理器"""
        try:
            # 确定日志目录
            if log_dir is None:
                log_dir = Path.cwd() / 'logs'
            else:
                log_dir = Path(log_dir)

            # 创建日志目录
            log_dir.mkdir(parents=True, exist_ok=True)

            # 生成日志文件名
            log_file = log_dir / f'{self.name}.log'

            # 使用RotatingFileHandler实现日志轮转
            file_handler = logging.handlers.RotatingFileHandler(
                filename=log_file,
                maxBytes=max_file_size,
                backupCount=backup_count,
                encoding='utf-8'
            )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(file_handler)

        except Exception as e:
            print(f"Failed to create file handler: {e}", file=sys.stderr)

    def debug(self, msg: str, *args, **kwargs):
        """记录调试信息"""
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        """记录一般信息"""
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        """记录警告信息"""
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        """记录错误信息"""
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        """记录严重错误信息"""
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg: str, *args, **kwargs):
        """记录异常信息（包含堆栈跟踪）"""
        self.logger.exception(msg, *args, **kwargs)


# 全局默认日志记录器
def setup_logger(
        name: str = 'app',
        log_dir: Optional[Union[str, Path]] = None,
        log_level: str = 'INFO',
        console_output: bool = True,
        file_output: bool = True,
        **kwargs
) -> Logger:
    """
    设置全局日志记录器

    Args:
        name: 日志记录器名称
        log_dir: 日志文件目录
        log_level: 日志级别
        console_output: 是否输出到控制台
        file_output: 是否输出到文件
        **kwargs: 其他参数传递给Logger类

    Returns:
        Logger实例
    """
    global LOG
    LOG = Logger(
        name=name,
        log_dir=log_dir,
        log_level=log_level,
        console_output=console_output,
        file_output=file_output,
        **kwargs
    )
    return LOG


# 创建默认全局日志记录器
LOG: Optional[Logger] = None
if LOG is None:
    LOG = Logger()
