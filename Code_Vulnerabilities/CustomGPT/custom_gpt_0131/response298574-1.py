
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to only one item as required
test[1] = '"'+test[1]+'"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    # Create a CSV writer object with minimal quoting
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Write the data to the CSV file
    csvOut.writerow(test)

# Print the test list to confirm
print(test)
# Expected output: ['item1', '"01"', '001', 1]
