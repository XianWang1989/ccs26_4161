
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the second item
test[1] = '"' + test[1] + '"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, escapechar='\\')

    # Write the row
    csvOut.writerow(test)

# Print for verification
print(test)
