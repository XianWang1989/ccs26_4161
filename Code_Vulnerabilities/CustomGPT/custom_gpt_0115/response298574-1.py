
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to a specific item
test[1] = '"'+test[1]+'"'

# Open the file
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print to verify the output
print(test)
