
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header
    for row in allrows:
        # Create a new row with only the desired columns
        filtered_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(filtered_row)
