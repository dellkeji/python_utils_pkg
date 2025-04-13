import socket
from typing import Optional


class Host:

    @classmethod
    def get_host_ip(cls) -> Optional[str]:
        """获取当前机器的 ip"""
        try:
            # 获取主机名
            hostname = socket.gethostname()
            # 获取IP地址
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except Exception:
            return ""
