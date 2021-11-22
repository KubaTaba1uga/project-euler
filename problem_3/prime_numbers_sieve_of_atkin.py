""" The alghoritm
    Create a results list, filled with 2, 3, and 5.

    Create a sieve list with an entry for each positive integer; all entries in this list should initially be marked non-prime.

    For each entry number n in the sieve list, with modulo-sixty remainder r:
        If r is 1, 13, 17, 29, 37, 41, 49, or 53, flip the entry for each possible solution to 4x2 + y2 = n.

        If r is 7, 19, 31, or 43, flip the entry for each possible solution to 3x2 + y2 = n.

        If r is 11, 23, 47, or 59, flip the entry for each possible solution to 3x2 – y2 = n when x > y.

        If r is something else, ignore it completely…

    Start with the lowest number in the sieve list.

    Take the next number in the sieve list, still marked prime.

    Include the number in the results list.

    Square the number and mark all multiples of that square as non-prime. Note that the multiples that can be factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.

    Repeat steps four through seven.

"""

MAXIMUM = 20

final_list = [2, 3, 5]
