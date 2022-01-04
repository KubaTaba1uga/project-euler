def is_prime(the_number):
    """As prime number has only two factors
    1 and itself, look for first three factors
    if there are found it is not prime number
    """
    factors_counter = 1
    for i in range(1, the_number):
        if the_number % i == 0:
            factors_counter += 1
            if factors_counter == 3:
                return False
    return True


def find_prime_numbers(max_value: int):
    for number in range(max_value + 1):
        if is_prime(number):
            print(number)
            yield number


prime_numbers = find_prime_numbers(2000000)

print("Sum of all primes below two milion is", sum(prime_numbers))
