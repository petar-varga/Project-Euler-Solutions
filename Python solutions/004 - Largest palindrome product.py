def check_if_palindrome(number_string):
    length_of_string = len(number_string)

    for i in range(0, int(length_of_string/2)):
        if number_string[i] == number_string[length_of_string-i-1]:
            #print("same")
            pass
        else:
            return False
    return True

valid_result = 0

for first_number in range(100, 1000):
    for second_number in range(100, 1000):
        possible_result = first_number * second_number

        if check_if_palindrome(str(possible_result)):

            if possible_result > valid_result:
                valid_result = possible_result

            print(valid_result)
    
print(valid_result)