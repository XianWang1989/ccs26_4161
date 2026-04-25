
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract the columns with at least one '1' (excluding the first column)
keepcols = [c for c in allrows[0] if c != "Title" and any(r[c] == '1' for r in allrows)]

# Write to new CSV file
with open("output1.csv", "w", newline='') as out_file:
    writer = csv.DictWriter(out_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        filtered_row = {k: row[k] for k in keepcols + ['Title']}
        writer.writerow(filtered_row)

print("Columns with '1's have been extracted to output1.csv")
