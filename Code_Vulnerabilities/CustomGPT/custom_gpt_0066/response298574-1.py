
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to a specific item
test[1] = '"{}"'.format(test[1])  # This adds quotes around '01'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print to verify the output
print(test)
