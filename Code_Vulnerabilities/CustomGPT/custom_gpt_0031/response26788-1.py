
import csv

with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Filter columns that contain at least one '1' (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Output the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    for row in allrows:
        new_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Filtered columns written to output1.csv")
