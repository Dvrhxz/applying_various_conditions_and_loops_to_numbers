# make list to store values
number_list = []

# ask for 10 inputs
for i in range(10):
    numbers = float(input(f"Input number {i + 1}: "))
    number_list.append(numbers)

# get the first number then subtract using the remaining numbers
first_number = number_list[0]

for numbers in number_list[1:]:
    first_number -= numbers

# print the result
print(f"number {number_list[0]} minus all the remaining numbers is equal to {first_number}")