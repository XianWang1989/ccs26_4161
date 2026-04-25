# Open the file in read+write binary mode
with open('yourfile.txt', 'r+b') as f:
    # Seek to the 4th byte (0-based index)
    f.seek(4)
    
    # Write new bytes in place
    f.write(b'01234')
