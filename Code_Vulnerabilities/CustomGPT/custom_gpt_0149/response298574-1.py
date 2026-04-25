
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Manually format the second item with quotes
test[1] = f'"{test[1]}"'

# Open the file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Printing for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
