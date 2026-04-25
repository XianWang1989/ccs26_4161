
with open('filename.txt', 'a+') as file:
    editor = YourEditorClass(file)
    line_count = editor.tell(char=True)
    print(f"Lines: {line_count}")
