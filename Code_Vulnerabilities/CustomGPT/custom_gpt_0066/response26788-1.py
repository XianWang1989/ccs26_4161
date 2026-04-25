
import csv

# Read the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (those with at least one '1')
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()

    for row in allrows:
        new_row = {c: row[c] for c in keepcols if c in row}
        new_row['Title'] = row['Title']  # Include the 'Title' column
        writer.writerow(new_row)
