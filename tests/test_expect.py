from gendiff.engine import generate_diff


def test_first_file_not_found():
    assert generate_diff("tests/fixtures/before_fail.json",
                         "tests/fixtures/after.json", "text") == 'File not found'

def test_extension():
    assert generate_diff("tests/fixtures/before.fail",
                         "tests/fixtures/after_fail.fail", "text") == 'Unsupported type of files'


def test_format():
    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "fail") == 'Incorrect output format'
