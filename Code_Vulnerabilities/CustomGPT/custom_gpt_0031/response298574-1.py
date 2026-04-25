
import csv

# Example data
test = ['item1', '01', '001', 1]

# Wrap the second item in double quotes
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes
    csvOut.writerow(test)

# Print for verification
print(test)
