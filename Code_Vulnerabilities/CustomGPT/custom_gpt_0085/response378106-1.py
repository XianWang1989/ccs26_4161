
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()  # Save current position
        self.f.seek(0)  # Seek to the beginning of the file
        line_count = 0
        line_position = current_position

        for line in self.f:
            if line_position >= len(line):
                line_position -= len(line)
                line_count += 1
            else:
                break

        self.f.seek(current_position)  # Restore the original position

        if char:
            return line_count, line_position
        return line_count

    def close(self):
        self.f.close()

# Example usage:
file_editor = FileEditor('example.txt')
line_count = file_editor.tell()
print(f'Number of lines: {line_count}')
file_editor.close()
