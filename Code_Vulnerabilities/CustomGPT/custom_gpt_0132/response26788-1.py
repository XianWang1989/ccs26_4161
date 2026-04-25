
import csv

# Open the input CSV file and read the data
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify the columns to keep (those with at least one '1')
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new dict containing only the columns to keep
        filtered_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(filtered_row)
