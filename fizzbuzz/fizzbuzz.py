"""
Write a program that prints one line for each number from 1 to 100
For multiples of three print Fizz instead of the number
For the multiples of five print Buzz instead of the number
For numbers which are multiples of both 3 and 5 print FizzBuzz instead of the number
"""


def fizzbuzz(n: int):
    for line_number in range(1, n + 1):
        print(line_number)


if __name__ == "__main__":
    fizzbuzz(100)
