
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that contain at least one '1' (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Verify that there are columns to write out
if keepcols:
    # Write to a new CSV file with the extracted columns
    with open("output1.csv", "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
        writer.writeheader()
        for row in allrows:
            # Create a new row filtered by keepcols
            new_row = {k: row[k] for k in keepcols if k in row}
            # Ensure to also include the Title column
            new_row['Title'] = row['Title']
            writer.writerow(new_row)
else:
    print("No columns with '1' found.")
