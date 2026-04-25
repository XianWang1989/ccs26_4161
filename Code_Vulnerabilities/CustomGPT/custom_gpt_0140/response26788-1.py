
import csv

# Open the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract column names where any value is '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare output with only the selected columns
filtered_rows = [{col: row[col] for col in keepcols} for row in allrows]

# Write filtered data to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    writer.writerows(filtered_rows)  # Write the filtered rows
