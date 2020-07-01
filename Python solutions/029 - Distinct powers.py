def get_list_of_integer_combinations(a_min, a_max, b_min, b_max):
    list_of_combinations = []

    for a in range(a_min, a_max+1):
        for b in range(b_min, b_max+1):
            list_of_combinations.append(a**b)
    
    return list_of_combinations

def remove_duplicates_from_list(list_object):
    return list(dict.fromkeys(list_object))

integer_combinations = get_list_of_integer_combinations(2, 100, 2, 100)
integer_combinations = remove_duplicates_from_list(integer_combinations)

print(len(integer_combinations))