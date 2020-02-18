from gendiff.engine import generate_diff


def test_plain():
    f_plain = open("tests/fixtures/result_plain.txt", "r")
    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "plain") == f_plain.read()
    f_plain.close()


def test_json():
    f_json = open("tests/fixtures/result_json.txt", "r")
    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "json") == f_json.read()
    f_json.close()


def test_text():
    f_text = open("tests/fixtures/result_text.txt", "r")
    assert generate_diff("tests/fixtures/before.json",
                         "tests/fixtures/after.json", "text") == f_text.read()
    f_text.close()


def test_plain_text():
    f_plain_text = open("tests/fixtures/result_plain_text.txt", "r")
    assert generate_diff("tests/fixtures/before_plain.json",
                         "tests/fixtures/after_plain.json", "text") == f_plain_text.read()
    f_plain_text.close()
