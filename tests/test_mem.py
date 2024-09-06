from utils.mem import MemoryUsage


# pytest -s tests/test_mem.py
def test_get_used_memory():
    print(f"{MemoryUsage.get_used_memory('initial')} MB")
    # 初始化占用数据
    [i for i in range(10000000)]
    print(f"after init data, {MemoryUsage.get_used_memory('after a created')} MB")
