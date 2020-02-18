from gendiff.engine import generate_diff


def test_expect():
    assert generate_diff("tests/fixtures/before_fail.json",
                         "tests/fixtures/after.json", "text") == 'File not found'

    assert generate_diff("tests/fixtures/before.fail",
                         "tests/fixtures/after_fail.fail", "text") == 'Unsupported type of files'

    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "fail") == 'Incorrect output format'
