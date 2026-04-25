
import csv

# Open the CSV file and read it
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Variable to keep track of columns with at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create a writer object for the output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()

    # Write the rows with only keepcols
    for row in allrows:
        new_row = {k: row[k] for k in keepcols}
        new_row['Title'] = row['Title']  # Keep the first column
        writer.writerow(new_row)
