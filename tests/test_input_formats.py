from gendiff.engine import generate_diff


def test_input_formats():
    with open("tests/fixtures/result_json.txt", "r") as result_json:
        assert generate_diff("tests/fixtures/before.yml",
                             "tests/fixtures/after.yml", "json") == result_json.read()

    with open("tests/fixtures/result_plain.txt", "r") as result_plain:
        assert generate_diff("tests/fixtures/before.json",
                             "tests/fixtures/after.json", "plain") == result_plain.read()
