
import csv

# Load CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare output data
output_data = [{col: row[col] for col in keepcols} for row in allrows]

# Write to new CSV file
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header
    writer.writerows(output_data)
