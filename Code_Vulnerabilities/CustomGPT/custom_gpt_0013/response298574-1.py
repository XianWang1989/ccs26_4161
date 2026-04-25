
import csv

# Example data
test = ['item1', '01', '001', 1]

# Wrap the second element in quotes
test[1] = '"' + test[1] + '"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
