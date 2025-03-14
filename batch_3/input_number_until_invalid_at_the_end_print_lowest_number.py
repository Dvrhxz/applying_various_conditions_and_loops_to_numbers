# loop asking for inputs
numbers_list = []
while True:
    try:
        number = int(input(f"Input a number: "))

        # find and print the lowest number from all inputs

    # end program when input is invalid
    except ValueError:
        print("That is invalid\nProgram will now stop...")
        break