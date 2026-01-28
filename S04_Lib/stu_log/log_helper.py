"""
日志快捷使用模块
提供导入即用的LOG对象
"""

import sys
from pathlib import Path
from log_encap import Logger, setup_logger

# 初始化全局日志记录器
LOG: Logger = setup_logger(
    name='app',
    log_dir=Path(__file__).parent/'logs',
    log_level='INFO',
    console_output=True,
    file_output=True
)

debug = LOG.debug
info = LOG.info
warning = LOG.warning
error = LOG.error
critical = LOG.critical
exception = LOG.exception

__all__ = [
    'LOG',
    'Logger',
    'setup_logger',
    'debug',
    'info',
    'warning',
    'error',
    'critical',
    'exception'
]
