
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with at least one '1'
keepcols = [c for c in allrows[0] if c == 'Title' or any(r[c] == '1' for r in allrows)]

# Create a new list of rows with only the selected columns
filtered_rows = [{c: r[c] for c in keepcols} for r in allrows]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(filtered_rows)
