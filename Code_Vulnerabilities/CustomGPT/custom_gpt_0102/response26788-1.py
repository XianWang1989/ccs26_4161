
import csv

# Open and read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare to write to the output file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row containing only the relevant columns
        new_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(new_row)
