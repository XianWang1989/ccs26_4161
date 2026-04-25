
# Open the file in 'r+b' mode to read and write binary data
with open('yourfile.txt', 'r+b') as f:
    # Move the file pointer to position (4, 0), which signifies byte offset 4
    f.seek(4)  

    # Write the new bytes '01234' at the specified position
    f.write(b'01234')
