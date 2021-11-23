number = 0
while True:
    number += 2
    checksum = [True for i in range(1, 20) if number % i == 0]
    print(number)
    if len(checksum) == 19:
        print('BANG', number)
        break
