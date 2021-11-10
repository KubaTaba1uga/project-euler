def generate_fibbonacci_numbers(stop_value, value_0=0, value_1=1, sum=0):
    if value_0 < stop_value:
        result = value_0 + value_1
        if result % 2 == 0:
            sum += result
        return generate_fibbonacci_numbers(stop_value, value_1, result, sum)
    else:
        return sum


result = generate_fibbonacci_numbers(4000000)

print('sum', result)
