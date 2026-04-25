
import csv

# Open the CSV file and read it using DictReader
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Identify columns that contain at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

print("Columns to keep:", keepcols)

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Create a new row dictionary that only includes the columns we want to keep
        new_row = {field: row[field] for field in keepcols + ['Title']}
        writer.writerow(new_row)
