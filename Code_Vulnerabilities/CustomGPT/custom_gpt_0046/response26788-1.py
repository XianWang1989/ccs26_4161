
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Include only the columns to keep
        output_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(output_row)
