from gendiff.engine import generate_diff


def test_yaml():
    f = open("tests/fixtures/result_json.txt", "r")
    assert generate_diff("tests/fixtures/before.yml",
                         "tests/fixtures/after.yml", "json") == f.read()
    f.close()


def test_json():
    f = open("tests/fixtures/result_plain.txt", "r")
    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "plain") == f.read()
    f.close()
