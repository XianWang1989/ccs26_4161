
import csv

# Reading the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extracting columns that contain only '1's
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Preparing to write to the output file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    # Writing relevant rows
    for row in allrows:
        output_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(output_row)
