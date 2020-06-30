import string

def get_names_in_list():
    with open("Python solutions/p022_names.txt", "r") as filename:
        text_from_file = filename.read()
        list_of_names = text_from_file.replace('"', "").split(",")
        return list_of_names

def get_name_worth(name):
    total_worth = 0
    for letter in name:
        total_worth = total_worth + string.ascii_lowercase.index(letter.lower()) + 1
    
    return total_worth

def get_summation_of_scores(sorted_names):
    summation = 0

    for index, name in enumerate(sorted_names):
        value_for_name = get_name_worth(name)
        summation = summation + (value_for_name * (index + 1))

    return summation

names = get_names_in_list()
names.sort()
print(get_summation_of_scores(names))


