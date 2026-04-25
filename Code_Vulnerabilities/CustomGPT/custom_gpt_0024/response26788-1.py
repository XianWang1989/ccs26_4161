
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the filtered rows to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the columns to keep
        new_row = {col: row[col] for col in keepcols}
        new_row['Title'] = row['Title']  # Include the Title column
        writer.writerow(new_row)
