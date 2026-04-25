
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1'
keepcols = [c for c in reader.fieldnames if any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # write the header
    for row in allrows:
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)

print("Filtered columns written to output1.csv")
