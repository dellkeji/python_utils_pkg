"""
copy module
copy files or dir from src to dest
"""
from pathlib import Path


def copy_file(src: str, dst: str) -> bool:
    """复制文件
    分下面几种场景
    - 源和目的都是文件
    - 源是文件，目的是目录
    - 源是目录，目的也是目录
    """
    # 检查源是文件还是目录
    pass


def _is_file(src: str) -> bool:
    """判断是否是文件"""
    obj = Path(src)
    return obj.is_file()


def _is_dir(src: str) -> bool:
    """判断是否是目录"""
    obj = Path(src)
    return obj.is_dir()
    