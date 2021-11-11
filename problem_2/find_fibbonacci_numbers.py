def find_fb_numbers(stop_value, value_0=0, value_1=1, fb_numbers=list()):
    if value_0 < stop_value:
        result = value_0 + value_1
        fb_numbers.append(result)
        return find_fb_numbers(stop_value, value_1, result, fb_numbers)
    else:
        return fb_numbers


result = find_fb_numbers(4000000)

print('result', result)
