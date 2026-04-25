
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header row

    for row in allrows:
        # Create a new row with only the columns we want to keep
        new_row = {key: row[key] for key in keepcols}
        new_row['Title'] = row['Title']
        writer.writerow(new_row)  # Write filtered row to the output file
