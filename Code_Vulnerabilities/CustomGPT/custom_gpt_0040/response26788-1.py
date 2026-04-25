
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Extract column names that contain at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare the output file
with open("output1.csv", "w", newline='') as f_output:
    writer = csv.DictWriter(f_output, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        # Include only the rows with kept columns
        output_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(output_row)

print(f"Extracted columns: {keepcols}")
