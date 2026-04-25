
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the specific item
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    # Write the row
    csvOut.writerow(test)

# Print to verify the output
print(test)
