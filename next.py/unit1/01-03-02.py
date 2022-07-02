def is_prime(number):
    return not any(True if not number % i else False for i in range(2, number // 2))


print(is_prime(2))
print(is_prime(23))
print(is_prime(29))
print(is_prime(42))
print(is_prime(43))
