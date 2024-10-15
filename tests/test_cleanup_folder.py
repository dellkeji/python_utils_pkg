from pathlib import Path
import shutil

import pytest

from utils.cleanup_folder import cleanup_folder

@pytest.fixture()
def create_and_delete_folder():
    paths = [
        Path("/tmp/test_folder"),
        Path("/tmp/test_folder/t1"),
        Path("/tmp/test_folder/t2"),
        Path("/tmp/test_folder/t3"),
        Path("/tmp/test_folder/t4"),
        Path("/tmp/test_folder/t5")
    ]
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)  # parents=True 表示如果父目录不存在，会一并创建
    yield
    # 清理环境
    shutil.rmtree("/tmp/test_folder")


def test_cleanup_folder(create_and_delete_folder):
    base_dir = "/tmp/test_folder"
    flag = cleanup_folder(folder_path=base_dir, keep_num=3,force=True)
    assert flag == True
    fp = Path(base_dir)
    subdirs = [d for d in fp.iterdir() if d.is_dir()]
    assert len(subdirs) == 3
