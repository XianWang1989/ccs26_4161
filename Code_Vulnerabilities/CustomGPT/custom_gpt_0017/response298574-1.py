
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the specific item
test[1] = f'"{test[1]}"'

# Open the CSV writer
with open('file.txt', 'a', newline='') as file:  # Use 'newline' to avoid extra newlines in Windows
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Change to QUOTE_MINIMAL

    # Write the row
    csvOut.writerow(test)

# Printing for verification
print(test)
