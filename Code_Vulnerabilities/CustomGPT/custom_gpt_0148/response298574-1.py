
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the specific item
test[1] = f'"{test[1]}"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print the output for debugging
print(test)
