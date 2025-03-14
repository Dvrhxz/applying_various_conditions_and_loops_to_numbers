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
        # print average
        # end program
        break
