
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Determine columns to keep
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Write to the output CSV
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header
    for row in allrows:
        writer.writerow({c: row[c] for c in keepcols})  # Write only the kept columns
