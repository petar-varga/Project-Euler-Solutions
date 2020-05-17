number_to_check = 20
while(True):
    for i in range(1,21):
        if number_to_check % i != 0:
            break
    if i == 20 and number_to_check % 20 == 0:
        break
    number_to_check = number_to_check + 20

print(number_to_check)