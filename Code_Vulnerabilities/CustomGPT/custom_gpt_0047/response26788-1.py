
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep that contain at least one '1'
keepcols = ['Title']  # Always keep the Title column
for c in allrows[0].keys():
    if c != 'Title' and any(r[c] == '1' for r in allrows):
        keepcols.append(c)

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header
    writer.writerows(allrows)

print("Columns saved in 'output1.csv':", keepcols)
