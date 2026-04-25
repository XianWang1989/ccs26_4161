
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the 'Title' and the selected columns
        new_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Columns with '1's saved to output1.csv")
