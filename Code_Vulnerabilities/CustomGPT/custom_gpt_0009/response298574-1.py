
import csv

# Test data
test = ['item1', '01', '001', 1]

# Open the output file with 'newline=""' to avoid extra newlines
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    # Adjust the second item in the list
    test[1] = '"'+test[1]+'"'  # Ensure it’s wrapped in quotes as intended

    print(test)  # prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # This will write without extra quotes
