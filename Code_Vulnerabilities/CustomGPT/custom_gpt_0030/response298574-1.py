
import csv

# Test data
test = ['item1', '01', '001', 1]

# Quote the desired item
test[1] = '"' + test[1] + '"'

# Open the output file with the desired mode
with open('file.txt', 'a', newline='') as f:
    # Create CSV writer with specific quoting
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # Print to console for verification
    print(test)  # Expected: ['item1', '"01"', '001', 1]

    # Write the row to CSV
    csvOut.writerow(test)

# Close is handled by 'with' block
