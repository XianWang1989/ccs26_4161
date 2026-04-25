
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the second item
test[1] = '"{}"'.format(test[1])

# Print the modified list
print(test)  # Prints: ['item1', '"01"', '001', 1]

# Open CSV file for appending and write data
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# File will now write: item1,"01",001,1
