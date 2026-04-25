
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes around only the second item
test[1] = f'"{test[1]}"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes

    # Write the row
    csvOut.writerow(test)

# Print to verify output
print(test)
