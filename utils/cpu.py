"""
cpu util module
make a util to calculate cpu usage of a process or system, and so on.
"""

import psutil


class CPUUsage:

    @classmethod
    def get_cpu_usage(cls) -> float:
        """获取 CPU使用率"""
        # 获取 CPU使用率
        cpu_percent = psutil.cpu_percent(interval=1)
        return cpu_percent
    
    @classmethod
    def get_process_cpu_usage(cls, pid: int) -> float:
        """获取知道进程的cpu使用率
        @param pid: 进程ID
        @return: 进程的CPU使用率
        """
        process = psutil.Process(pid)

        # 获取进程的CPU使用率
        cpu_usage = process.cpu_percent(interval=1)
        return cpu_usage
