
import csv

# Read the data from the CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Determine the columns to keep (those that have at least one '1')
keepcols = ['Title']  # Always keep the first column
for c in allrows[0].keys():
    if c != 'Title' and any(r[c] == '1' for r in allrows):
        keepcols.append(c)

# Prepare data for output
output_rows = [{col: row[col] for col in keepcols} for row in allrows]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keepcols)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"Kept columns: {keepcols}")
