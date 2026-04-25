
editor = FileEditor('example.txt')
line_count = editor.tell()  # Get line count up to the current position
print(f'Lines counted: {line_count}')

line_count, char_pos = editor.tell(char=True)  # Get both line count and char position
print(f'Lines counted: {line_count}, Character position in line: {char_pos}')

editor.close()
