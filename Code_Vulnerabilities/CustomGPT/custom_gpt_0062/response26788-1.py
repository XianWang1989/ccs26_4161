
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = ['Title']  # Always keep the first column
keepcols.extend(c for c in allrows[0] if any(r[c] == '1' for r in allrows))

# Write the new CSV file with the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()
    for row in allrows:
        filtered_row = {col: row[col] for col in keepcols}
        writer.writerow(filtered_row)
