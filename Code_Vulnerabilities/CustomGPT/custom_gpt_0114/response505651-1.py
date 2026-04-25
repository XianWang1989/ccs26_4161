
lineToWrite = ""

for company in line:
    if company == 'XXX':
        continue  # Skip this iteration if company is 'XXX'
    else:
        lineToWrite += company + "\t"  # Append the company to the lineToWrite

print(lineToWrite)
