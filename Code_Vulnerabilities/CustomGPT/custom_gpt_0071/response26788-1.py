
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine columns to keep
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()

    for row in allrows:
        # Create a new dictionary for each row with only the columns to keep
        output_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(output_row)

print("Extraction completed. Check output1.csv for results.")
