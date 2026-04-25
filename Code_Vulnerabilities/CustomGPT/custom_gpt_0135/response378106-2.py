
file_editor = FileEditor("example.txt")

# Use the tell function to get line and character position
line_count, char_pos = file_editor.tell(char=True)
print(f"Line: {line_count}, Character Position: {char_pos}")

# Remember to close the file
file_editor.close()
