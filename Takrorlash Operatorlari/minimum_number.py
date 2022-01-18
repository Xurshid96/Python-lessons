# eng kattasini topish
numbers = [10, 3, 7, 32, 25, 13]

min_number = 0
for number in numbers:
    if min_number < number:
        min_number = number

print("maxsimum nuber: ", min_number)

#  eng kichigini topish
numbers = [10, 3, 7, 32, 25, 13]

min_number = numbers[0]
for number in numbers:
    if min_number > number:
        min_number = number

print("minimum nuber: ", min_number)