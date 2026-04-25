
import csv

# Test data
test = ['item1', '01', '001', 1]

# Preprocess the second item to add quotes without triggering extra quotes
test[1] = f'"{test[1]}"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print the output to verify
print(test)  # Should print: ['item1', '"01"', '001', 1]
