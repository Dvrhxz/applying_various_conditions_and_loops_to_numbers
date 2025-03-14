# loop ask for input
numbers_list = []

while True:
    try:
        number = int(input("Input a number: "))
        numbers_list.append(number)

    # if input invalid print sorted list and end program
    except ValueError:
        print("\nThe numbers sorted from lowest to highest is:")
        print(sorted(numbers_list))
        break