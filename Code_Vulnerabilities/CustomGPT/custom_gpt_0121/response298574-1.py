
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the second item
test[1] = f'"{test[1]}"'

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check the output
print(test)
