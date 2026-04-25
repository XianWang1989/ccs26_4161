
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the CSV file and write the row
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    csvOut.writerow(test)

# For verification, let's print the result
print(test)
