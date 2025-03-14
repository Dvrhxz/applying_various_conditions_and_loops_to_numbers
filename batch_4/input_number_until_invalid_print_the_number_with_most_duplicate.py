# ask for looping inputs
while True:
    try:
        number = int(input("Input number: "))
# when input is invalid print number with most duplicates
    # end program
    except ValueError:
        print("\nThat is invalid\nProgram will now stop...")
        break