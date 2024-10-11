from pathlib import Path
import shutil

import pytest


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


def test_cleanup_folder():
    pass
