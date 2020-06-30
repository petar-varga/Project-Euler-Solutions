import itertools

def get_list_of_permutations(list_of_values):
    return list(itertools.permutations(list_of_values))

list_of_values = []
for i in range(0, 10):
    list_of_values.append(i)

all_permutations = get_list_of_permutations(list_of_values)

print("".join(str(x) for x in all_permutations[999_999]))
#2783915460