
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding double quotes to a single item in the list
test[1] = '"{}"'.format(test[1])

# Open the file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    print(test)  # Prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Output will be: item1,"01",001,1
