
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with at least one '1' (excluding the first column)
keepcols = [col for col in reader.fieldnames[1:] if any(row[col] == '1' for row in allrows)]

# Prepare to write the output file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)

    # Write the header
    writer.writeheader()

    # Write the rows with only selected columns
    for row in allrows:
        output_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(output_row)
