# make for loop printing numbers 0-100
for numbers in range (0,101):
    # exclude printing numbers ending in 0
    if numbers %10 !=0:
        print (numbers)