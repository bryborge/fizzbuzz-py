from src.fizzbuzz import create

# Arrange, Act
FIZZ_BUZZ_ARR = create(15)


def test_fizzbuzz_replaces_all_numbers_divisible_by_three_with_fizz():
    # Assert
    assert FIZZ_BUZZ_ARR[2] == "Fizz"
    assert FIZZ_BUZZ_ARR[5] == "Fizz"
    assert FIZZ_BUZZ_ARR[8] == "Fizz"
    assert FIZZ_BUZZ_ARR[11] == "Fizz"


def test_fizzbuzz_replace_all_numbers_divisible_by_five_with_buzz():
    # Assert
    assert FIZZ_BUZZ_ARR[4] == "Buzz"
    assert FIZZ_BUZZ_ARR[9] == "Buzz"


def test_fizzbuzz_replaces_all_numbers_divisible_by_three_and_five_with_fizzbuzz():
    # Assert
    assert FIZZ_BUZZ_ARR[14] == "FizzBuzz"
