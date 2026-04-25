
import csv

# Open the CSV file and read the data
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keep columns that have at least one '1'
keepcols = [c for c in allrows[0].keys() if any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(({c: row[c] for c in keepcols} for row in allrows))  # Filter columns for each row
