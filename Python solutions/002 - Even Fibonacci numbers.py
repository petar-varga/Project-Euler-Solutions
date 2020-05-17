summation = 0

first_previous = 0
second_previous = 1
result = 0

while(first_previous + second_previous <= 4_000_000):
    result = first_previous + second_previous
    if result % 2 == 0:
        summation = summation + result
    first_previous = second_previous
    second_previous = result

print(summation)