
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1', excluding the first column (titles)
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create a new list of rows containing only the selected columns
filtered_rows = [{col: row[col] for col in keepcols if col in row} for row in allrows]

# Write to the output CSV file
with open("output1.csv", "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    writer.writerows(filtered_rows)
