
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that contain at least one '1' (except the first column)
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        filtered_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(filtered_row)

print("Filtered columns have been written to output1.csv")
