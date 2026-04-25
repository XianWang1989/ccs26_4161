
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create a new list of rows with only the selected columns
filtered_rows = [{col: row[col] for col in keepcols} for row in allrows]

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    writer.writerows(filtered_rows)
