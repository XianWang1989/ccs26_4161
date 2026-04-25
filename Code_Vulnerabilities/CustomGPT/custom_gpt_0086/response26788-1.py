
import csv

# Read the CSV file
with open("test1.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write the filtered result to a new CSV file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        filtered_row = {k: row[k] for k in keepcols if k in row and row[k] == '1'}
        writer.writerow({'Title': row['Title'], **filtered_row})
