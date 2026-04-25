
import csv

def escape_quotes(item):
    # Return item as is if it doesn't contain quotes
    if '"' in item:
        return item  # Handle or escape appropriately, if needed.
    return '"' + item + '"'  # Add quotes around the value

# Test data
test = ['item1', '01', '001', 1]

# Escape the second item explicitly
test[1] = escape_quotes(test[1])

# Open CSV file in append mode
with open('file.txt', 'a', newline='') as file:
    # Create a csv writer with minimal quoting
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    # Write the row to the file
    csvOut.writerow(test)

# Print to verify
print(test)  # Expected: ['item1', '"01"', '001', 1]
