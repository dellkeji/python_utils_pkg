"""
os tools module

This module provides some useful functions for operating system.
"""

import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path


def cleanup_folder(folder_path: str, keep_num: int = 3,  keep_days: int = 7, force: bool = False) -> bool:
    """删除指定路径的文件夹，保留数量优先级高于时间
    - 会存在这样一种场景: 不在保留的数量内，但是不满足删除时间的内容
    
    @param folder_path: 要删除的文件夹路径
    @param keep_days: 保留最近多少天的文件夹，默认保留7天
    @param keep_num: 保留最多多少个文件夹，默认保留3个
    @param force: 是否强制删除，默认不强制，如果开启强制，则不在数量之内的文件夹，都进行删除
    @return: 是否成功删除
    """
    # 将字符串路径转换为 Path 对象
    pf = Path(folder_path)
    
    # 确保文件夹存在
    if not pf.exists() or not pf.is_dir():
        print(f"the path {folder_path} does not exist or is not a directory.")
        return False
    
    sub_folders = sorted([item for item in pf.iterdir() if item.is_dir()], key=lambda x: x.stat().st_mtime)
    # 获取需要保留的文件夹数量
    print(f"keep folders: {sub_folders[-keep_num:]}")
    
    now_time = datetime.now()
    # 删除超出保留时间的文件夹
    for folder in sub_folders[:-keep_num]:
        # 获取文件夹的修改时间
        mod_time = datetime.fromtimestamp(folder.stat().st_mtime)
        # 计算文件夹最后修改时间与当前时间的差值
        if now_time - mod_time < timedelta(days=keep_days) and not force:
            print(f"folder {folder} is not out of date, skip.")
            continue
        # 递归删除文件夹，包含文件夹下的所有内容
        print(f"deleting folder: {folder}")
        shutil.rmtree(folder)
    
    return True

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python cleanup_folder.py <folder_path> <keep_num> <keep_days> <force>")
        sys.exit(1)
    folder_path_str = sys.argv[1]
    keep_num = int(sys.argv[2])
    keep_days = int(sys.argv[3])
    force = sys.argv[4] == "True" or sys.argv[4] == "true"

    cleanup_folder(folder_path_str, keep_num, keep_days, force)