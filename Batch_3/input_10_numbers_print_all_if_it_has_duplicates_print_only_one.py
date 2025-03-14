# make 10 inputs and store in list
numbers_list = []

for i in range (10):
    number = int(input(f"Input number {i + 1}: "))
    numbers_list.append(number)

# print number, if it has duplicates print it once only
numbers_first_entry = []
already_in_numbers_first_entry = set()

for number in numbers_list:
    if number not in already_in_numbers_first_entry:
        numbers_first_entry.append(number)
        already_in_numbers_first_entry.add(number)

print(f"Numbers inputted without reiteration is: {numbers_first_entry}")