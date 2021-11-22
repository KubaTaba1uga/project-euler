A = 999
B = 999
MAXIMUM = A * B


def is_palindrome(number):
    return str(number) == str(number)[::-1]

palidromes = set()
for i in range(A, 100, -1):
    for j in range(B, 100, -1):
        if is_palindrome(i * j) and i * j < MAXIMUM:
            palidromes.add(i * j)


print("Maximum", max(palidromes))
