
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0
        self.f.seek(0)

        # Iterate through the lines without causing the OSError
        for line in self.f:
            line_length = len(line)
            if current_position >= line_length:
                current_position -= line_length
                line_count += 1
            else:
                break

        if char:
            return line_count, current_position
        return line_count

    def close(self):
        self.f.close()

# Example usage:
file_editor = FileEditor('example.txt')
print(file_editor.tell())  # Returns number of lines
print(file_editor.tell(char=True))  # Returns number of lines and character position
file_editor.close()
