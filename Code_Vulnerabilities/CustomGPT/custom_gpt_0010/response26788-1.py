
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        filtered_row = {key: row[key] for key in keepcols if key in row}
        if any(row[key] == '1' for key in keepcols):
            writer.writerow({"Title": row["Title"], **filtered_row})

print("Extraction complete. Check 'output1.csv'.")
