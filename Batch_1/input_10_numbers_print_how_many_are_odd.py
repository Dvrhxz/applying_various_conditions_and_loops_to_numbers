# make list to store inputs for odds and evens
odd_numbers = []
even_numbers = []

# input 10 numbers
for i in range (10):
    inputs = float(input(f"input number {i + 1}: "))
    # if number odd, add to odd list
    if inputs %2 != 0:
        odd_numbers.append(inputs)
    # if number even, add to even list
    else:
        even_numbers.append(inputs)

# count and print the amount off odd numbers in the list
