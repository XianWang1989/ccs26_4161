
editor = FileEditor('example.txt')

# Example of using the tell function
line_number = editor.tell()
print("Current line number: ", line_number)

# Don't forget to close the file after usage
editor.close()
