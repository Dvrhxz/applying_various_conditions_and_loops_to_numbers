# print numbers 0-100
for numbers in range(0, 101):
    # print only numbers not ending in 5 or 0
    if numbers %5 != 0:
        print(numbers)