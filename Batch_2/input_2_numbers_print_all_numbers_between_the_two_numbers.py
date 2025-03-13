# input 2 numbers
first_num = int(input("Input the 1st number: "))
second_num = int(input("Input the 2nd number: "))

# print numbers between the two
num_after_first = min(first_num, second_num) + 1
num_before_second = max(first_num, second_num)

print(f"the numbers between {first_num} and {second_num} are")
for numbers in range(num_after_first, num_before_second):
    print(numbers)