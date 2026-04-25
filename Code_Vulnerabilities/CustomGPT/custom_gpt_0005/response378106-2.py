
editor = FileEditor('example.txt')

# Adding some content to the file
with open('example.txt', 'a') as f:
    f.write('First line\nSecond line\nThird line\n')

# Using the tell function
line_count = editor.tell()
print(f'Current line count: {line_count}')

editor.close()
