
import csv

# Read CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare to write to output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    # Write only the rows with selected columns
    for row in allrows:
        filtered_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(filtered_row)
