def count_squares_sum(r_boundary):
    return sum(i**2 for i in range(1, r_boundary + 1))


def count_sums_squares(r_boundary):
    return sum(range(1, r_boundary + 1))**2


def show_result(r_boundary):
    squares_sum = count_squares_sum(r_boundary)
    sum_squares = count_sums_squares(r_boundary)

    print(f'{sum_squares} - {squares_sum} = {sum_squares - squares_sum}')

show_result(100)
