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


for i in range(2, 30):
    print(i, is_prime(i))


def find_n_prime(n):
    """ Find n prime numbers
    """
    i = 2
    prime_counter = 0
    while True:
        if is_prime(i):
            prime_counter += 1
            print(prime_counter, i)
            if prime_counter == n:
                return i
        i += 1

find_n_prime(10001)
