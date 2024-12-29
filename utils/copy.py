"""
copy module
copy files or dir from src to dest
"""
import os
import shutil
from typing import Optional

from pathlib import Path


def copy_file(src: str, dst: str, is_dst_file: Optional[bool] = False) -> bool:
    """复制文件
    分下面几种场景
    - 源和目的都是文件
    - 源是文件，目的是目录
    - 源是目录，目的也是目录
    """
    # 检查原路径存在
    if not os.path.exists(src):
        # TODO: 可以记录日志或者直接抛出异常
        return False
    # 检查源是文件还是目录


def _copy_dir(src: str, dst: str) -> bool:
    """拷贝目录下的内容到指定的目录"""
    pass


def _copy_file(src: str, dst: str, is_dst_file: Optional[bool] = False) -> bool:
    """拷贝文件到指定位置"""
    dst_path = Path(dst)
    # 检测目录是否存在，不存在，则创建
    if not os.path.exists(dst):
        dst_path.parent.mkdir(parents=True, exist_ok=True)
    # 拷贝文件
    shutil.copy(src, dst)
    return True


def _is_file(src: str) -> bool:
    """判断是否是文件"""
    obj = Path(src)
    return obj.is_file()


def _is_dir(src: str) -> bool:
    """判断是否是目录"""
    obj = Path(src)
    return obj.is_dir()
    