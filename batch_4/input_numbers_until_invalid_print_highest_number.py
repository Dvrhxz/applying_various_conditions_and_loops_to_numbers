# ask for inputs until invalid
while True:
    try:
        number = int(input("Input a number: "))

    # when invalid print results
    except ValueError:
        print("\nThat is invalid\nProgram will now print the highest number")
        # end program
        break

