
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (those that have at least one '1')
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create output CSV file with the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()
    for row in allrows:
        # Create a new row with only the columns we want to keep
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Extraction complete. Check output1.csv for results.")
