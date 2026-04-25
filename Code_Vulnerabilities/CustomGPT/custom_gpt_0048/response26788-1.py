
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Identify columns to keep (those that have at least one '1')
keepcols = [c for c in allrows[0] if c != "Title" and any(r[c] == '1' for r in allrows)]

# Create a new list of dictionaries with only the kept columns
filtered_rows = [{c: row[c] for c in keepcols} for row in allrows]

# Write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Title"] + keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(filtered_rows)
