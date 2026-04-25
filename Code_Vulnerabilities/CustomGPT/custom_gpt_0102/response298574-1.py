
import csv

# Define your test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the second item
test[1] = '"01"'

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')
    csvOut.writerow(test)

# Print to verify the output
print(test)
