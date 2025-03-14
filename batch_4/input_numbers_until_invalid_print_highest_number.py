# ask for inputs until invalid
numbers_list = []
while True:
    try:
        number = int(input("Input a number: "))
        numbers_list.append(number)

    # when invalid print results
    except ValueError:
        print("\nThat is invalid\nProgram will now print the highest number")
        print(f"The highest number inputted is: {max(numbers_list)}")

        # end program
        break