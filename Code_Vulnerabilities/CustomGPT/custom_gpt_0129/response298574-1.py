
import csv

# Original test data
test = ['item1', '01', '001', 1]

# Add quotes to a single item (as desired)
test[1] = '"01"'  # We want this formatted as is, with the quotes

# Open the file with write mode
with open('file.txt', 'a', newline='') as f:
    # Create a CSV writer with QUOTE_MINIMAL to avoid blank rows
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    # If you want to ensure quotes inside quotes are handled correctly
    # Replace the existing quotes
    test[1] = test[1].replace('"', '""')  # Escape the inner quotes

    # Write the row
    csvOut.writerow(test)

# The resulting output in 'file.txt' should be: item1,"01",001,1
