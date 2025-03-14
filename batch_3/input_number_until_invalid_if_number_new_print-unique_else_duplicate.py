# make loop to ask for inputs
while True:
    try:
        number = int(input(f"Input a number: "))

    # when input invalid end program
    except ValueError:
        print("That is invalid\nProgram will now stop...")
        break

# while program running if input is new say "unique" if not "duplicate"

