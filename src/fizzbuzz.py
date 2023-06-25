# Fizz Buzz Module

def calculate(num: int) -> list:
    arr = []
    for n in range(1, num + 1):
        if _fizzy(n) and _buzzy(n):
            arr.append('FizzBuzz')
        elif _fizzy(n):
            arr.append('Fizz')
        elif _buzzy(n):
            arr.append('Buzz')
        else:
            arr.append(n)
    return arr


def _fizzy(n: int) -> bool:
    return n % 3 == 0


def _buzzy(n: int) -> bool:
    return n % 5 == 0
