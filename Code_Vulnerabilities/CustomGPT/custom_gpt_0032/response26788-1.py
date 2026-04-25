
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare data for output file: keep only necessary columns
filtered_rows = [{k: r[k] for k in keepcols} for r in allrows]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()
    writer.writerows(filtered_rows)

print("Extraction complete. Check output1.csv.")
