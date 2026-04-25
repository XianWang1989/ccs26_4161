
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (other than the first column)
keepcols = [col for col in reader.fieldnames[1:] if any(row[col] == '1' for row in allrows)]

# Prepare output by selecting only the necessary columns
output_rows = [{key: row[key] for key in keepcols} for row in allrows]

# Write to new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()
    writer.writerows(output_rows)
