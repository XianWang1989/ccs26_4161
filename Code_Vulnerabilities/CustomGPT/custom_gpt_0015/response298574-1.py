
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the desired field in quotes directly
test[1] = '\"' + test[1] + '\"'  # This adds the quotes directly without extra ones

# Open CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Using QUOTE_MINIMAL to handle quotes correctly
    csvOut.writerow(test)

# Print to verify
print(test)
