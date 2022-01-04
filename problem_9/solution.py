for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a + b + c == 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    print(f"{a}* {b}* {c} == {a*b*c}")
