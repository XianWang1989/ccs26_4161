
lineToWrite = ""

for x in line:
    if x == 'XXX':
        continue
    else:
        lineToWrite += x + "\t"

# Output the result
print(lineToWrite)
