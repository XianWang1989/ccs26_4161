
import csv

# Test data
test = ['item1', '01', '001', 1]

# Modify the string to include quotes
test[1] = '"' + test[1] + '"'

# Open the file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
    csvOut.writerow(test)

# Check the output
print(test)  # Prints: ['item1', '"01"', '001', 1]
