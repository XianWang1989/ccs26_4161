
line = ['Company A', 'Company B', 'XXX', 'Company D']
lineToWrite = ""

for company in line:
    if company == 'XXX':
        continue
    else:
        lineToWrite += company + "\t"

print(lineToWrite.strip())
