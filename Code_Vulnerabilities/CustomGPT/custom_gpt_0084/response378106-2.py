
editor = FileEditor('example.txt')
print(editor.tell())  # Returns line count based on current position
editor.close()        # Always ensure to close the file
