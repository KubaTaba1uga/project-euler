from prime_numbers_sieve_of_eratostenes import get_prime_numbers_gen as get_prime_numbers

NUMBER = 600851475143


prime_number_list = get_prime_numbers(NUMBER)

factorials = []
for prime_number in prime_number_list:
    if NUMBER % prime_number == 0:
        NUMBER = NUMBER / prime_number
        factorials.append(prime_number)

print(factorials)
