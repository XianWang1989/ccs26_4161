
import csv

# Original test data
test = ['item1', '01', '001', 1]

# To add quotes around the string without causing extra quotes in output
test[1] = '"' + test[1] + '"'

# Use csv.QUOTE_MINIMAL to only quote fields that contain special characters
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Checking the print output
print(test)  # Output: ['item1', '"01"', '001', 1]
