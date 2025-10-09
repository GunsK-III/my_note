#  开发一个数据库连接池。外部使用者只需要get_connection()和release_connection(conn)，
#  而不需要关心池的大小如何管理、连接如何创建和销毁、空闲连接的超时处理等复杂逻辑。

class ConnectionPool:
    def __init__(self, max_connections=10):
        self._max_connections = max_connections
        self._available_connections = []
        self._in_use_connections = set()
        # ... 其他复杂的初始化逻辑

    def _create_connection(self):
        # 创建新连接的复杂逻辑
        pass

    def get_connection(self):
        """对外提供的简洁接口"""
        if not self._available_connections and len(self._in_use_connections) < self._max_connections:
            self._available_connections.append(self._create_connection())
        # ... 复杂的连接获取和状态管理逻辑
        conn = self._available_connections.pop()
        self._in_use_connections.add(conn)
        return conn

    def release_connection(self, conn):
        """对外提供的简洁接口"""
        if conn in self._in_use_connections:
            self._in_use_connections.remove(conn)
            self._available_connections.append(conn)
        # ... 可能的连接健康检查和清理逻辑


# 使用：接口非常简单清晰
pool = ConnectionPool(max_connections=5)
conn = pool.get_connection()
# ... 使用连接
pool.release_connection(conn)

