
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item without extra quotes in the output
test[1] = '"{}"'.format(test[1])  # Alternatively: test[1] = f'"{test[1]}"'

# Open CSV file
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output should now be: item1,"01",001,1
