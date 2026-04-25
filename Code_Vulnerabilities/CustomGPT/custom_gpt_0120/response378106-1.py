
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()

        # Seek to the beginning to count lines
        self.f.seek(0)
        line_count = 0
        remaining_chars = current_position

        for line in self.f:
            if remaining_chars >= len(line):
                remaining_chars -= len(line)
                line_count += 1
            else:
                break

        # Reset the file pointer back to the original position
        self.f.seek(current_position)

        if char:
            return line_count, remaining_chars
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Returns the line count up to the current position
editor.close()
