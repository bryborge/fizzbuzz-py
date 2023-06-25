# Fizz Buzz Module

def calculate(num: int) -> list:
    arr = []
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            arr.append('FizzBuzz')
        elif n % 3 == 0:
            arr.append('Fizz')
        elif n % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(n)
    return arr


class FizzBuzz:
    pass
