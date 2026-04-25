
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Extract columns with at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the output file with the selected columns
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        writer.writerow({col: row[col] for col in ['Title'] + keepcols})

print(f"Columns extracted: {keepcols}")
