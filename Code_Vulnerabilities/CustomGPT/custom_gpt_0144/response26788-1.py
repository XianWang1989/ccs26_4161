import csv

# Read all rows from CSV
with open("test1.csv", "r", newline='') as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine columns to keep — those with at least one '1'
keepcols = [col for col in reader.fieldnames if any(row[col] == '1' for row in allrows)]

# Write the filtered columns to new CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(allrows)
