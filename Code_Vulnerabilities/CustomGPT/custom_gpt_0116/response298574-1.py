
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding quotes to the desired item
test[1] = '"' + test[1] + '"'

# Open the CSV file using 'a' for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL
    csvOut.writerow(test)

# Printing for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
