
import csv

# Open the CSV file and read the contents
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Determine which columns have at least one '1'
keepcols = [c for c in allrows[0] if c != "Title" and any(r[c] == '1' for r in allrows)]

# Create a new list of rows with only the selected columns
filtered_rows = [{col: row[col] for col in keepcols if col in row} for row in allrows]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Title"] + keepcols)
    writer.writeheader()
    writer.writerows(filtered_rows)

print("Columns with 1's extracted and written to output1.csv.")
