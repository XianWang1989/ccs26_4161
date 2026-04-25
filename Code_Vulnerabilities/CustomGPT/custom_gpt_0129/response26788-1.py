
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that contain at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows if r[c] != '0')]

# Create a new file to write the extracted columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header
    # Write only the columns that are in keepcols
    for row in allrows:
        filtered_row = {c: row[c] for c in keepcols}  # Filter the row to include only keepcols
        writer.writerow(filtered_row)

print("Extraction complete. Check output1.csv for the result.")
