
import csv

# Open the CSV file and read all rows
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Extract column names (excluding the first column)
column_names = list(allrows[0].keys())
keepcols = [c for c in column_names[1:] if any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the kept columns
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)
