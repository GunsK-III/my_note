from log_helper import LOG

def main():
    LOG.info("应用程序启动")
    LOG.debug("调试信息")
    LOG.warning("警告信息")
    LOG.error("错误信息")

    try:
        result = 1 / 0
        return result
    except Exception as e:
        LOG.exception("发生异常: %s", str(e))

    LOG.info("应用程序结束")


if __name__ == "__main__":
    main()
