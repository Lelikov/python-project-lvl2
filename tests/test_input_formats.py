from gendiff.engine import generate_diff


def test_input_formats():
    with open("tests/fixtures/plain.golden", "r") as result_json:
        assert generate_diff("tests/fixtures/before.yml",
                             "tests/fixtures/after.yml", "plain") == result_json.read()

    with open("tests/fixtures/plain.golden", "r") as result_plain:
        assert generate_diff("tests/fixtures/before.json",
                             "tests/fixtures/after.json", "plain") == result_plain.read()
