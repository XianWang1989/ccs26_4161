
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Manually wrap the second item with double quotes
test[1] = '"{}"'.format(test[1])

# Open file in append mode and create csv writer
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes
    csvOut.writerow(test)  # Write the row

# Print to check output
print(test)
