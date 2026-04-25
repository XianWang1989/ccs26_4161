
lineToWrite = ""

# Sample data
line = ['ABC', 'XXX', 'DEF', 'XXX', 'GHI']

for x in line:
    if x == 'XXX':
        continue
    else:
        lineToWrite += x + "\t"

print(lineToWrite)  # Output: ABC    DEF    GHI    
