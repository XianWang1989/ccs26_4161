
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Find columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header row
    for row in allrows:
        # Create a new row that only includes desired columns
        new_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Extracted columns:", keepcols)
