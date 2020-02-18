from gendiff.engine import generate_diff


def test_output_formats():
    with open("tests/fixtures/result_plain.txt", "r") as result_plain:
        assert generate_diff("tests/fixtures/before.json",
                             "tests/fixtures/after.json", "plain") == result_plain.read()

    with open("tests/fixtures/result_json.txt", "r") as result_json:
        assert generate_diff("tests/fixtures/before.json",
                             "tests/fixtures/after.json", "json") == result_json.read()

    with open("tests/fixtures/result_text.txt", "r") as result_text:
        assert generate_diff("tests/fixtures/before.json",
                             "tests/fixtures/after.json", "text") == result_text.read()

    with open("tests/fixtures/result_plain_text.txt", "r") as result_plain_text:
        assert generate_diff("tests/fixtures/before_plain.json",
                             "tests/fixtures/after_plain.json", "text") == result_plain_text.read()
