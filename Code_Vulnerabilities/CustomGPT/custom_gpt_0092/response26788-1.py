
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        new_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(new_row)
