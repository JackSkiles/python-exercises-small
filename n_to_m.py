
# Asks user for starting number and ending number to loop through.
starting_number = input('Please input the number you would like to start at: ')
starting_number = int(starting_number)

ending_number = input('Please input the number you would like to end on: ')
ending_number = int(ending_number)

# Prints starting number + 1 as long as it is less than the ending number entered.
while starting_number <= ending_number:
    print(starting_number)
    starting_number += 1
