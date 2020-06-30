def get_factorial(number):
    result = 1
    for i in range(2, number+1):
        result = result * i
    return result

def get_sum_of_digits(number):
    summary = 0
    for single_number in str(number):
        summary = summary + int(single_number)
    return summary

result_of_factorial = get_factorial(100)
sum_of_digits = get_sum_of_digits(result_of_factorial)
print(sum_of_digits)