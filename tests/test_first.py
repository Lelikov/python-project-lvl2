from gendiff.engine import generate_diff

def test_diff():
    f = open("tests/fixtures/result.txt", "r")
    assert generate_diff("tests/fixtures/before.json", "tests/fixtures/after.json") == f.read()
    f.close()
