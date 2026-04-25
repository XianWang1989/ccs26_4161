
lineToWrite = ""

# Example list of companies
companies = ['AAA', 'XXX', 'BBB', 'CCC']

for x in companies:
    if x == 'XXX':
        continue  # Skip this iteration if company is 'XXX'
    else:
        lineToWrite += x + "\t"

print(lineToWrite)  # Output will be: AAA    BBB    CCC
