
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that contain only 1s (except the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Create the output CSV with only the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the selected columns
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)
