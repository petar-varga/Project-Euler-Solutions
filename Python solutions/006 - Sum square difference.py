def sum_of_squares(count):
    summation = 0
    for i in range(1, count+1):
        summation = summation + (i*i)
    return summation

def square_of_sum(count):
    summation = 0
    for i in range(1, count + 1):
        summation = summation + i
    return summation * summation

print(square_of_sum(100) - sum_of_squares(100))