# make 10 inputs and store in list
numbers_list = []

for i in range (10):
    number = int(input(f"Input number {i + 1}: "))
    numbers_list.append(number)

# print number, if it has duplicates print it once only