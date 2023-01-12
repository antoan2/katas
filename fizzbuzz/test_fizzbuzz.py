import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("line_number, expected", [(1, "1"), (719, "719")])
def test_get_line_number_repr(line_number, expected):
    assert fizzbuzz.get_line_number_repr(line_number) == expected


def test_fizzbuzz(capsys):
    fizzbuzz.fizzbuzz(2)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n"
