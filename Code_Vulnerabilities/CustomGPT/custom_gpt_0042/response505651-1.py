
line = ['Company1', 'XXX', 'Company2', 'Company3']  # Example list
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue  # Skip this iteration if Company is 'XXX'

    lineToWrite += x + "\t"  # Append the company to the line

print(lineToWrite)  # Output: Company1	Company2	Company3	
