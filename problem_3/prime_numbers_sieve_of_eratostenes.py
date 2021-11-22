# Sieve of Eratostenes implementation
""" The alghoritm
        Let us take an example when n = 50. So we need to print all prime numbers smaller than or equal to 50.
        We create a list of all numbers from 2 to 50.
        According to the algorithm we will mark all the numbers which are divisible by 2 and are greater than or equal to the square of it.
        Now we move to our next unmarked number 3 and mark all the numbers which are multiples of 3 and are greater than or equal to the square of it.
        We move to our next unmarked number 5 and mark all multiples of 5 and are greater than or equal to the square of it.
        ...
"""


def check_multi(control_number, to_check):
    """ Check if a number is a multiple of another number
    """
    print(f'{to_check} % {control_number}', to_check % control_number)
    print(f'{to_check} > {control_number}', to_check > control_number)
    return to_check % control_number == 0 and to_check > control_number


def get_prime_numbers_list(looking_for):
    """ Get prime numbers as list
    """
    all_numbers = [i for i in range(2, looking_for)]
    for i in all_numbers:
        for z in range(i, looking_for):
            if check_multi(i, z):
                try:
                    all_numbers.pop(all_numbers.index(z))
                except ValueError:
                    pass
    return all_numbers


def get_prime_numbers_gen(looking_for):
    """ Get prime numbers as generator
    """
    all_numbers = (i for i in range(2, looking_for))
    not_prime_numbers = set()
    for i in all_numbers:
        for z in range(i, looking_for):
            if check_multi(i, z):
                    """ Get not prime numbers without duplicates
                    """
                    not_prime_numbers.add(z)

    for i in (i for i in range(2, looking_for)):
        """ Generate prime numbers
        """
        if i not in not_prime_numbers:
            yield i
