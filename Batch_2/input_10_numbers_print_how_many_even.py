# make list to store evens and odds
even_list = []
odd_list = []

# input 10 numbers and store in list
for i in range(10):
    numbers = float(input(f"Input number {i + 1}: "))
    if numbers %2 == 0:
        even_list.append(numbers)
    else:
        odd_list.append(numbers)

print(even_list)
print(odd_list)

# print the amount of values stored in evens list
