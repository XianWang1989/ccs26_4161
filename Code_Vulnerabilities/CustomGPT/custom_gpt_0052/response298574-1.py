
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in double quotes
test[1] = '01'  # No need to manually add quotes here

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting
    # Write the row to the CSV
    csvOut.writerow(test)

# Print for verification
print(test)
