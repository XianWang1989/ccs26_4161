
# Open the file in 'ab+' mode
with open('yourfile.txt', 'ab+') as file:
    # Seek to the position (4, 0) which is offset 4
    file.seek(4)

    # Replace "issom" with "01234"
    file.write(b'01234')
