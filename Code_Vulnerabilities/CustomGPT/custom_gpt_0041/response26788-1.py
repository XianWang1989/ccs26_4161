
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep (all `1`s except for the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to a new CSV file
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        # Create a new dictionary with only the columns to keep
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)

print(f"Columns kept: {keepcols}")
