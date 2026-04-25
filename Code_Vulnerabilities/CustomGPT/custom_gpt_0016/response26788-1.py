
import csv

# Open and read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep (those where all values are '1')
keepcols = ['Title']  # Start with the title column
for c in allrows[0].keys():
    if c != 'Title' and all(r[c] == '1' for r in allrows):
        keepcols.append(c)

# Create a new CSV file to write the output
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header row
    for row in allrows:
        # Only write rows with the columns we want to keep
        writer.writerow({c: row[c] for c in keepcols})

print(f'Columns kept: {keepcols}')
