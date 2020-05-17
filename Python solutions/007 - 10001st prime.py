import math
number_to_check = 2
counter = 1
while(True):
    is_prime = True

    for i in range(2, math.ceil(math.sqrt(number_to_check)) + 1):
        if number_to_check % i == 0:
            is_prime = False
            break

    if is_prime:
        counter = counter + 1
        if counter == 10_001:
            break

    number_to_check = number_to_check + 1


print("10 001:", number_to_check)