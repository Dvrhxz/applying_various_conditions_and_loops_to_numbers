# make 10 inputs and store into list
numbers_list = []

for i in range(10):
    number =int(input(f"Input number {i + 1}: "))
    numbers_list.append(number)

# check if number only entered once
no_duplicates = []

for number in numbers_list:
    if numbers_list.count(number) == 1:
        no_duplicates.append(number)

# print number that only appears once
print(f"The numbers that have no duplicates are as follows: {no_duplicates}")