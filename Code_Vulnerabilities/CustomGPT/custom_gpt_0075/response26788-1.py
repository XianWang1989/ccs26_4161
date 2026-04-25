
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with at least one '1' (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row containing only the columns we want
        new_row = { 'Title': row['Title'] }
        for col in keepcols:
            new_row[col] = row[col]
        writer.writerow(new_row)
