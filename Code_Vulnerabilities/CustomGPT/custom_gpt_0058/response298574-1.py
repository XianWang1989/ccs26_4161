
import csv

# test "data"
test = ['item1', '01', '001', 1]

# Open the output file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    # Add quotes to the specific item
    test[1] = '"'+test[1]+'"'

    # Print the modified list
    print(test)  # Prints: ['item1', '"01"', '001', 1]

    # Write the modified row to the csv file
    csvOut.writerow(test)

# The output in 'file.txt' will now be: item1,"01",001,1
