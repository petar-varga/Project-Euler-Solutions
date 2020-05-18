def sequence_count(starting_number):
    current_number = starting_number
    count = 1

    while(current_number != 1):
        if current_number % 2 == 0:
            current_number = current_number / 2
        else:
            current_number = 3 * current_number + 1
        count = count + 1 

    return count

max_starting_number = 1_000_000
longest_chain = 1
starting_number = 1
for i in range(1, max_starting_number):
    count_for_current_number = sequence_count(i)
    if count_for_current_number > longest_chain:
        longest_chain = count_for_current_number
        starting_number = i

print(starting_number)
