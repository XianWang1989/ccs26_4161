
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep based on the condition of having '1's
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create output CSV and write the rows with only the columns we want
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()  # Write the header row
    for row in allrows:
        new_row = {key: row[key] for key in ['Title'] + keepcols}  # Retain selected columns
        writer.writerow(new_row)
