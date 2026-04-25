
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (only those with at least one '1')
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create a new list of filtered rows
filtered_rows = [{col: row[col] for col in keepcols} for row in allrows]

# Write to output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(filtered_rows)  # Write the filtered rows
