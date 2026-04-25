
with open('example.txt', 'a+') as f:
    f.write('First line\nSecond line\nThird line\n')

    # Create an instance of your class (assuming your class is called FileEditor)
    editor = FileEditor('example.txt')

    # Use the tell method
    line_count = editor.tell()
    print(f'Number of lines before position: {line_count}')
