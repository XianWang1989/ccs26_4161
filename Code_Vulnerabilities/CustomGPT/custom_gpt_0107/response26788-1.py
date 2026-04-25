
import csv

# Read the CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Identify columns where all values are not '0'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    for row in allrows:
        output_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(output_row)
