
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"' + test[1] + '"'

# Open the file with 'a' mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL, quotechar='"')

    # Write the row
    csvOut.writerow(test)

# To verify output, let's print the list
print(test)  # Output will be: ['item1', '"01"', '001', 1]
