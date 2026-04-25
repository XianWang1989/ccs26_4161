
import csv

# Test data
test = ['item1', '01', '001', 1]

# Modify the second item in the list (without extra quotes)
test[1] = '01'  # Keep it just as '01'

# Open CSV file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting
    csvOut.writerow(test)

# Output the current list to the console
print(test)
