
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    for row in allrows:
        # Create new row with only the kept columns
        new_row = { 'Title': row['Title'] }
        new_row.update({c: row[c] for c in keepcols})
        writer.writerow(new_row)

print(keepcols)
