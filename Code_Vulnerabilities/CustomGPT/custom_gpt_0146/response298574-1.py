
import csv

# Preparing the data
test = ['item1', '01', '001', 1]

# Manually adding quotes to the second item
test[1] = '"01"'  # Adding quotes directly

# Opening the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    # Writing the row to the CSV file
    csvOut.writerow(test)

# Demonstrating the expected output in the print statement
print(test)  # This will print: ['item1', '"01"', '001', 1]
