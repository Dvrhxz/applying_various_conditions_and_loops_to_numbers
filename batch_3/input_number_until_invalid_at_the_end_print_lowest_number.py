# loop asking for inputs
numbers_list = []
while True:
    try:
        number = int(input("Input a number: "))
        numbers_list.append(number)

    # end program when input is invalid
    except ValueError:
        # find and print the lowest number from all inputs
        print("\nThat is invalid\nProgram will now print the lowest number")
        print(f"The lowest number is: {min(numbers_list)}")
        break