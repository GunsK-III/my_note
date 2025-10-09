from rocketmq.client import PushConsumer, ConsumeStatus


def print_message(msg):
    """简单的消息打印回调函数"""
    try:
        # 打印消息ID、主题和内容
        print(f"\n=== 收到消息 ===")
        print(f"消息ID: {msg.id}")
        print(f"主题: {msg.topic}")
        print(f"标签: {msg.tags}")
        print(f"消息体: {msg.body.decode('utf-8')}")
        print(f"生成时间: {msg.born_timestamp}")
        print(f"=== 消息结束 ===\n")

        return ConsumeStatus.CONSUME_SUCCESS
    except Exception as e:
        print(f"处理消息出错: {e}")
        return ConsumeStatus.RECONSUME_LATER


def consume_messages():
    """启动消费者"""
    consumer = PushConsumer('test_consumer_group')
    consumer.set_name_server_address('your_nameserver:9876')  # 替换为实际NameServer地址
    consumer.subscribe('your_topic', print_message)  # 替换为实际主题

    print("开始监听消息，按Ctrl+C停止...")
    consumer.start()

    try:
        # 保持运行
        while True:
            pass
    except KeyboardInterrupt:
        consumer.shutdown()
        print("\n消费者已停止")


if __name__ == '__main__':
    consume_messages()

