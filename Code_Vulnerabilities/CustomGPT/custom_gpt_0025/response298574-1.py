
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the second item in the list
test[1] = '"{}"'.format(test[1])  # Quotes around '01'
print(test)  # Output: ['item1', '"01"', '001', 1]

# Write to CSV file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check written output in the file
