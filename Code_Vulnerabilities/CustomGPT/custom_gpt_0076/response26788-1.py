
import csv

# Open the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that contain only '0's in all rows (except the first column)
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Print the columns you wish to keep
print(keepcols)

# Open the output CSV file to write the filtered columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the columns to keep
        new_row = {key: row[key] for key in keepcols}
        new_row['Title'] = row['Title']  # Include the first column
        writer.writerow(new_row)
