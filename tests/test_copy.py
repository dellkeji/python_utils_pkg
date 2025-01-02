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
    src_path1 = "/tmp/test/test1.txt"
    with open(src_path1, "w") as f:
        f.write("test1")
    # 删除文件
    yield
    os.remove(src_path)
    os.remove(src_path1)


def test_copy_file(create_and_delete_file):
    src_path = "/tmp/test/test.txt"
    dst_path = "/tmp/test1"
    copy_file(src_path, dst_path)

    assert os.path.exists(dst_path+"/test.txt")

    src_path = "/tmp/test/test1.txt"
    dst_path = "/tmp/test1/test1.txt"
    copy_file(src_path, dst_path, is_dst_file=True)
    assert os.path.exists(dst_path)
