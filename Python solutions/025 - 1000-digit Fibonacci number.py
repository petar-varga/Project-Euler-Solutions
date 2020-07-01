def count_digits_in_number(number):
    number = str(number)
    return len(number)

first_previous = 0
second_previous = 1
result = 0

term_index = 1

while(True):
    term_index = term_index + 1
    result = first_previous + second_previous
    if count_digits_in_number(result) == 1000:
        break
    first_previous = second_previous
    second_previous = result

print(term_index)