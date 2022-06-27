import functools

def sum_of_digits(number):
    return functools.reduce(lambda a, b: a + b, list(map(lambda x: int(x) % 10, str(number))))


if __name__ == "__main__":
    print(sum_of_digits(104))