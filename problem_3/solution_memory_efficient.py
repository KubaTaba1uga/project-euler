def find_factors(the_number):
    for i in range(2, the_number):
        if the_number % i == 0:
            yield i


def is_prime(the_number):
    """ As prime number has only two factors
            1 and itself, look for first three factors
            if there are found it is not prime number
    """
    factors_counter = 0
    for i in range(1, the_number):
        if the_number % i == 0:
            factors_counter += 1
            if factors_counter == 2:
                return False
    return True


def find_prime_factors(the_number):
    for factor in find_factors(NUMBER):
        if is_prime(factor):
            yield factor

NUMBER = 600851475143

for prime_factor in find_prime_factors(NUMBER):
    print("Prime factor:", prime_factor)
