import collections
from collections import Counter

# ask for looping inputs
numbers_list = []
while True:
    try:
        number = int(input("Input number: "))
        numbers_list.append(number)

    # end program after printing results
    except ValueError:

        # when input is invalid print number with most duplicates
        instances_of_number = Counter(numbers_list)

        number_with_most_duplicates = max(instances_of_number, key=instances_of_number.get)
        duplicate_amount = instances_of_number[number_with_most_duplicates]

        print("\nThat is invalid\nProgram will now show results")
        print(f"\nThe number with the most duplicates is {number_with_most_duplicates}"
              f" which was inputted {duplicate_amount} times")
        
        break