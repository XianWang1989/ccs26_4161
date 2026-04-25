
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the specific item as needed
test[1] = f'"{test[1]}"'

# Open the file for appending and write CSV
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to handle quotes properly
    csvOut.writerow(test)

# Print to verify result
print(test)
