from fizzbuzz import fizzbuzz


def test_fizzbuzz(capsys):
    fizzbuzz.fizzbuzz(2)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n"
