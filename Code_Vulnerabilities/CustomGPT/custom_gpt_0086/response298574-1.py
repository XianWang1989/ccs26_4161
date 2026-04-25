
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes around '01'
test[1] = '"{}"'.format(test[1])  # Using format to ensure it's a proper string

# Open file and create CSV writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    # Write the row
    csvOut.writerow(test)

# Print to confirm
print(test)  # Output will be: ['item1', '"01"', '001', 1]
