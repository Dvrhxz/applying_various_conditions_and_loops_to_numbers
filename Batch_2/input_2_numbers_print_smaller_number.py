# input 2 numbers
first_num = float(input("Input the 1st number: "))
second_num = float(input("Input the 2nd number: "))

# check which number is smaller
if first_num < second_num:
    # print the smaller number
    print(f"The number {first_num} is smaller than {second_num}")
else:
    print(f"The number {second_num} is smaller than {first_num}")