# ask 10 inputs
numbers_list = []
for i in range(10):
    number = int(input(f"input number {i + 1}: "))
    numbers_list.append(number)

# print numbers that have duplicates
duplicates = set()
first_entry_number = set()

for number in numbers_list:
    if number in first_entry_number:
        duplicates.add(number)
    else:
        first_entry_number.add(number)

print(f"All the numbers with duplicates are {list(duplicates)}")