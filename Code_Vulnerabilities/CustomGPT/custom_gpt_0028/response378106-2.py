
editor = FileEditor("example.txt")

# Assuming example.txt has several lines
line_count = editor.tell()
print(f"Number of lines before position: {line_count}")

editor.close()
