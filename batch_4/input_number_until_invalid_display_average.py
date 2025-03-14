# make list to store values
numbers_list = []

# ask for inputs
while True:
    try:
        number = int(input("input a number: "))
        numbers_list.append(number)

    # stop asking for inputs when invalid
    except ValueError:
        # calculate average
        sum_of_list = sum(numbers_list)
        average = sum_of_list / len(numbers_list)

        # print average
        print(f"\nThe average of all inputs is: {average}")

        # end program
        break
