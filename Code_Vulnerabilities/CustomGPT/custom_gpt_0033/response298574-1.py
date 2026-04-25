
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in quotes
test[1] = '"{}"'.format(test[1])  # Using format to add quotes

# Open the CSV file with the 'a' mode to append
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Write the row to the CSV
    csvOut.writerow(test)

# Print for verification
print(test)  # Output should be: ['item1', '"01"', '001', 1]
