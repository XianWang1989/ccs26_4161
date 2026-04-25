
import csv

# Read the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify the columns to keep (those that contain at least one '1')
keepcols = ['Title']  # Start with the first column
for column in allrows[0].keys():
    if column != 'Title' and any(row[column] == '1' for row in allrows):
        keepcols.append(column)

# Write the output CSV file with the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        writer.writerow({col: row[col] for col in keepcols})

print("Columns with '1's have been extracted to 'output1.csv'.")
