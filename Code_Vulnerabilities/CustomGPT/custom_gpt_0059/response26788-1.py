
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        new_row = {k: row[k] for k in keepcols}
        new_row['Title'] = row['Title']  # Include the 'Title' column
        writer.writerow(new_row)

print(f"Columns with '1's: {keepcols}")
