import os

import pytest

from utils.copy import copy_file


@pytest.fixture
def create_and_delete_file():
    # 创建文件
    os.makedirs("/tmp/test", exist_ok=True)
    src_path = "/tmp/test/test.txt"
    with open(src_path, "w") as f:
        f.write("test")
    # 删除文件
    yield
    os.remove(src_path)


def test_copy_file(create_and_delete_file):
    src_path = "/tmp/test/test.txt"
    dst_path = "/tmp/test1"
    copy_file(src_path, dst_path)

    assert os.path.exists(dst_path+"/test.txt")
