# input numbers until invalid and store to list
numbers_list = []

while True:
    try:
        number = int(input("Input a number: "))
        numbers_list.append(number)

    # when invalid stop asking input
    except ValueError:
        # print sorted list
        # end program
        break