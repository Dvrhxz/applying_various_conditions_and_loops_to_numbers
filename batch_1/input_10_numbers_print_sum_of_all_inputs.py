# make a list to store inputs
summation = []

# input 10 numbers
for i in range (10):
    inputs = float(input(f"Input number {i + 1}: "))
    summation.append(inputs)

# add all numbers in the list
result_summation = sum(summation)

# print results
print(f"The sum of all 10 numbers is equal to {result_summation}")