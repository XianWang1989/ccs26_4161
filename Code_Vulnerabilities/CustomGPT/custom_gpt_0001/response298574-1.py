
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually quote the second item in the list without introducing triples
test[1] = '"{}"'.format(test[1])  # Enclose the value in double quotes 

# Open the file and create the CSV writer
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    print(test)  # This will print: ['item1', '"01"', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)
