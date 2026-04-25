
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Find columns with at least one '1'
keepcols = [col for col in allrows[0].keys() if col != 'Title' and any(row[col] == '1' for row in allrows)]

# Extract the rows containing only the selected columns
extracted_data = [{col: row[col] for col in keepcols} for row in allrows]

# Write the output to the new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(extracted_data)
