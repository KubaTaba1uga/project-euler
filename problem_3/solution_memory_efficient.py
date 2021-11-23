def find_factors(the_number):
    for i in range(2, the_number):
        if the_number % i == 0:
            yield i


def is_prime(the_number):
    """ As prime number has only two factors
            1 and itself, check factors length
    """
    for element, i in enumerate(find_factors(the_number)):
        if i > 1:
            return False
    return True


def find_prime_factors(the_number):
    for factor in find_factors(NUMBER):
        if is_prime(factor):
            yield factor

NUMBER = 600851475143

for prime_factor in find_prime_factors(NUMBER):
    print("Prime factor:", prime_factor)