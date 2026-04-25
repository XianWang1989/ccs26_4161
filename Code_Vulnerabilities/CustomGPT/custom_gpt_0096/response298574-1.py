
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open file for writing
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    # Write the row
    csvOut.writerow(test)

# Printing for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
