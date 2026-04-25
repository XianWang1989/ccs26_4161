
editor = FileEditor('myfile.txt')
line_count = editor.tell()
print(f"Current line count: {line_count}")
editor.close()
