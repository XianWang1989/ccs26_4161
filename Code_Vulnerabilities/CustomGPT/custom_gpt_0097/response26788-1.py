
import csv

# Open the input file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (those with at least one '1')
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the output file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    for row in allrows:
        # Create a new row with only the columns to keep
        filtered_row = {key: row[key] for key in keepcols if key in row}
        filtered_row['Title'] = row['Title']  # Preserve 'Title'
        writer.writerow(filtered_row)
