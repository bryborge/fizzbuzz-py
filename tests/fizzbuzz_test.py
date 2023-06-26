from fizzbuzz import create


def test_fizzbuzz_replaces_all_numbers_divisible_by_three_with_fizz():
    # Arrange, Act
    fb = create(15)
    # Assert
    assert fb[2] == 'Fizz'
    assert fb[5] == 'Fizz'
    assert fb[8] == 'Fizz'
    assert fb[11] == 'Fizz'


def test_fizzbuzz_replace_all_numbers_divisible_by_five_with_buzz():
    # Arrange, Act
    fb = create(15)
    # Assert
    assert fb[4] == 'Buzz'
    assert fb[9] == 'Buzz'


def test_fizzbuzz_replaces_all_numbers_divisible_by_three_and_five_with_fizzbuzz():
    # Arrange, Act
    fb = create(15)
    # Assert
    assert fb[14] == 'FizzBuzz'
