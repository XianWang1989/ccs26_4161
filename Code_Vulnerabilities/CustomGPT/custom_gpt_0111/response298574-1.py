
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the specific item in quotes
test[1] = '"' + test[1] + '"'

# Open the file and create a CSV writer with custom quoting
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print to verify output
print(test)  # Output: ['item1', '"01"', '001', 1]
