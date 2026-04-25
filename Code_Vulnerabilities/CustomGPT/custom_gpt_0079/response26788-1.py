
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [
    c for c in allrows[0]  # Loop through columns
    if all(r[c] != '0' for r in allrows) and c != 'Title'  # Check if all values are '1'
]

# Write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        writer.writerow(row)  # Write rows with selected columns
