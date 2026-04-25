
import csv

reader = csv.DictReader(open("test1.csv", "r"))
allrows = list(reader)

keepcols = [c for c in allrows[0] if all(int(r[c]) == 1 for r in allrows)]

with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Title"] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        filtered_row = {k: row[k] for k in keepcols if k in row}
        writer.writerow({**{"Title": row["Title"]}, **filtered_row})

print("Extracted columns with 1s have been written to output1.csv.")
