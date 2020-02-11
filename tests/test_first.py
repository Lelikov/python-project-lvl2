from gendiff.engine import generate_diff

def test_diff_json():
    f = open("tests/fixtures/result.txt", "r")
    assert generate_diff("tests/fixtures/before.json", "tests/fixtures/after.json") == f.read()
    f.close()

def test_diff_yaml():
    f = open("tests/fixtures/result.txt", "r")
    assert generate_diff("tests/fixtures/before.yml", "tests/fixtures/after.yml") == f.read()
    f.close()