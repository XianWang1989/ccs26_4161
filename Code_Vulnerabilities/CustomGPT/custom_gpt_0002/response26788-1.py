
import csv

# Read CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with 1's
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write to output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(allrows)
