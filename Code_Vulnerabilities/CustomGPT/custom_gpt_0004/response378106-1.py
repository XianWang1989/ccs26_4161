
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()
        line_count = 0
        # Seek to the beginning of the file
        self.f.seek(0)

        try:
            # Iterate over lines in the file
            for line in self.f:
                if current_position >= len(line):
                    current_position -= len(line)
                    line_count += 1
                else:
                    break
        finally:
            # Restore the original position
            self.f.seek(current_position)

        if char:
            return line_count, current_position
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_position = editor.tell()
print(f"Current line: {line_position}")
editor.close()
