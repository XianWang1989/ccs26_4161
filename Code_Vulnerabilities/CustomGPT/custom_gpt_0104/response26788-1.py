
import csv

# Open the CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Determine which columns to keep (i.e., those that have at least one '1')
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Open the output CSV file
with open("output1.csv", "w", newline='') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header (column names)
    writer.writerows(allrows)

print("Columns kept:", keepcols)
