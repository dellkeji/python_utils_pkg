import os
import pytest
from utils.find import find_string_in_files

@pytest.fixture
def create_test_files(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f1 = d / "hello.txt"
    f1.write_text("hello world")
    f2 = d / "another.txt"
    f2.write_text("python is awesome")
    f3 = d / "empty.txt"
    f3.write_text("")
    # Create a file with non-utf8 encoding to test error handling
    f4 = d / "binary_file.bin"
    f4.write_bytes(b'\x80\x81\x82')
    return str(d)

def test_find_string_in_files(create_test_files):
    test_dir = create_test_files

    # Test case 1: String exists in one file
    found = find_string_in_files("hello", test_dir)
    assert len(found) == 1
    assert os.path.basename(found[0]) == "hello.txt"

    # Test case 2: String exists in another file
    found = find_string_in_files("awesome", test_dir)
    assert len(found) == 1
    assert os.path.basename(found[0]) == "another.txt"

    # Test case 3: String does not exist
    found = find_string_in_files("not_found_string", test_dir)
    assert len(found) == 0

    # Test case 4: Search in empty file
    found = find_string_in_files("", test_dir)
    # An empty string is technically in every file, so we expect all text files
    assert len(found) == 3
    file_names = [os.path.basename(f) for f in found]
    assert "hello.txt" in file_names
    assert "another.txt" in file_names
    assert "empty.txt" in file_names
