
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract the columns that contain only 1's (except the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Write the output CSV with the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        new_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Columns extracted:", keepcols)
