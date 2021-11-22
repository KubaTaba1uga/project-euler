# Sieve of Eratostenes implementation
def check_multi(control_number, to_check):
    """ Check if a number is a multiple of another number
    """
    print(f'{to_check} % {control_number}', to_check % control_number)
    print(f'{to_check} > {control_number}', to_check > control_number)
    return to_check % control_number == 0 and to_check > control_number

looking_for = 13195

all_numbers = [i for i in range(2, looking_for)]
prime_numbers = set()
for i in all_numbers:
    for z in range(i, looking_for):
        if check_multi(i, z):
            try:
                all_numbers.pop(all_numbers.index(z))
            except ValueError:
                pass

print(prime_numbers)
