
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the file and use csv.writer with appropriate quoting
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# For checking output
print(test)  # Should print: ['item1', '"01"', '001', 1]
