import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "line_number, expected",
    [
        (1, "1"),
        (719, "719"),
        (3, "Fizz"),
        (333, "Fizz"),
        (5, "Buzz"),
        (515, "Buzz"),
        (15, "FizzBuzz"),
        (555, "FizzBuzz"),
    ],
)
def test_get_line_number_repr(line_number, expected):
    assert fizzbuzz.get_line_number_repr(line_number) == expected


def test_fizzbuzz(capsys):
    fizzbuzz.fizzbuzz(15)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "\n".join(
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ]
        )
        + "\n"
    )
