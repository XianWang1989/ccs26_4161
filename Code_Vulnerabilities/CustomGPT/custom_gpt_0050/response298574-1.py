
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes around the second item
test[1] = '"{}"'.format(test[1])  # or test[1] = f'"{test[1]}"'
print(test)  # prints: ['item1', '"01"', '001', 1]

# Open the file and create a CSV writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)  # Write the modified test list

# Check the contents of 'file.txt' for the expected output
