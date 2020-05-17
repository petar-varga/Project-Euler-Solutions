import math
number_to_check = 2
summation = 7

while(number_to_check < 2_000_000):
    is_prime = True

    if number_to_check % 2 == 0 or number_to_check % 5 == 0:
        number_to_check = number_to_check + 1
        continue

    for i in range(3, math.ceil(math.sqrt(number_to_check))+1):
        if number_to_check % i == 0:
            is_prime = False
            break

    if is_prime:
        summation = summation + number_to_check

    number_to_check = number_to_check + 1

print("Sum:", summation)