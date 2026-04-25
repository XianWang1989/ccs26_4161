
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that have only 1's (except the first column)
keepcols = [c for c in allrows[0].keys() if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Write only the extracted columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        new_row = {key: row[key] for key in ['Title'] + keepcols}  # Include only the keepcols and the Title
        writer.writerow(new_row)
