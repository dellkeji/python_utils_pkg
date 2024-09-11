"""
memory util module
make a util to calculate memory usage of a process or system, and so on.
"""

import os

import psutil
from memory_profiler import profile


class MemoryUsage:

    @classmethod
    def get_used_memory(cls, hint: str = "rss"):
        """获取当前占用的内存"""
        # 获取当前进程 ID
        pid = os.getpid()
        p = psutil.Process(pid)

        info = p.memory_full_info()
        # 返回 MB
        memory = info.uss / 1024.0 / 1024
        return memory

    # %memit init_number()
    @classmethod
    @profile
    def init_number(cls):
        n = 100000
        a = [1] * n
        return a
