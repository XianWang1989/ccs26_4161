
import csv

# Test data
test = ['item1', '01', '001', 1]

# Format the desired item with quotes
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print for verification
print(test)  # Should print: ['item1', '"01"', '001', 1]
