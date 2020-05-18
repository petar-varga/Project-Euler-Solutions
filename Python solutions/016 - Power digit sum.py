import math

result = int(math.pow(2, 1000))
string_representation = str(result)

summation = 0

for digit in string_representation:
    summation = summation + int(digit)
    
print(summation)