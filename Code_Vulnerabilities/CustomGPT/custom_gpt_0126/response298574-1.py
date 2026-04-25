
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"'+test[1]+'"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print for verification (optional)
print(test)
