from pathlib import Path
from log_encap import setup_logger

# 自定义配置
LOG = setup_logger(
    name='myapp',
    log_dir=Path(__file__).parent/'logs',
    log_level='DEBUG',
    console_output=True,
    file_output=True,
    max_file_size=5 * 1024 * 1024,  # 5MB
    backup_count=10
)

def process_data():
    LOG.info("开始处理数据")
    # ... 处理逻辑
    LOG.debug("数据处理完成")
    LOG.info("数据已保存，共处理 %d 条记录", 100)


if __name__ == "__main__":
    process_data()