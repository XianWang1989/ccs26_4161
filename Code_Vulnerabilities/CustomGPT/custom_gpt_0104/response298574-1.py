
import csv

# Initial test data
test = ['item1', '01', '001', 1]

# Wrap the specific item in quotes without modifying it directly in the list
formatted_test = [test[0], f'"{test[1]}"', test[2], test[3]]

# Open a CSV file for appending
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

    # Write the formatted test data row
    csvOut.writerow(formatted_test)

# To verify, print the formatted_test
print(formatted_test)  # This will show: ['item1', '"01"', '001', 1]
