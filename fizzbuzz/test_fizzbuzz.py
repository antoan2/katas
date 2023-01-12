from fizzbuzz import fizzbuzz


def test_get_line_number_repr():
    assert fizzbuzz.get_line_number_repr(1) == "1"


def test_fizzbuzz(capsys):
    fizzbuzz.fizzbuzz(2)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n"
