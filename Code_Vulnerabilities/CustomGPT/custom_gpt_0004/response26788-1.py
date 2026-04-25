
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns that contain only '1'
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Create a new list of dictionaries with only the specified columns
filtered_rows = [{col: row[col] for col in keepcols} for row in allrows]

# Write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(filtered_rows)
