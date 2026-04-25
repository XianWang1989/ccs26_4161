
editor = FileEditor('example.txt')
# Do some operations
line_count = editor.tell()
print(f"Current position is at line: {line_count}")
editor.close()
