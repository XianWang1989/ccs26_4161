
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [col for col in allrows[0] if any(r[col] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols[1:], extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        filtered_row = {col: row[col] for col in keepcols}
        writer.writerow(filtered_row)
