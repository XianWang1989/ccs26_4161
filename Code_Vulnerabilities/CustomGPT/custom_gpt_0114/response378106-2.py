
editor = FileEditor('example.txt')

# Write some lines to the file
editor.f.write("First line\nSecond line\nThird line\n")
editor.f.flush()

# Get the current line count and position
line_count = editor.tell()
print("Number of lines:", line_count)

# Clean up
editor.close()
