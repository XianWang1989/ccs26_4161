
import csv

# Function to handle quoting correctly
def quote_item(item):
    if isinstance(item, str) and '"' in item:
        # Escape existing quotes
        item = item.replace('"', '""')
    return f'"{item}"' if isinstance(item, str) else str(item)

# Data list
test = ['item1', '01', '001', 1]
# Modify item with quotes as necessary
test[1] = quote_item(test[1])

# Write to CSV
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check output
print(test)  # Expected: ['item1', '"01"', '001', 1]
