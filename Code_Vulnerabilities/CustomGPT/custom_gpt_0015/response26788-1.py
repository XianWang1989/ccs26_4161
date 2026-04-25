
import csv

# Reading the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extracting the columns with at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Writing the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    # Write only the rows that have the required columns
    for row in allrows:
        filtered_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(filtered_row)

print("Extraction complete! Check 'output1.csv' for results.")
