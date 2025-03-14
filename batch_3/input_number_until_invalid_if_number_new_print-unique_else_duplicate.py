# make loop to ask for inputs
number_already_entered = set()
while True:
    try:
        number = int(input(f"\nInput a number: "))

        # while program running if input is new say "unique" if not "duplicate"
        if number not in number_already_entered:
            print("Unique")
            number_already_entered.add(number)
        else:
            print("Duplicate")

    # when input invalid end program
    except ValueError:
        print("That is invalid\nProgram will now stop...")
        break



