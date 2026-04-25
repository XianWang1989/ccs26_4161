
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Remember the current position
        current_position = self.f.tell()

        # Seek to the beginning of the file
        self.f.seek(0)

        # Initialize line counter and remaining bytes
        lc = 0
        remaining_bytes = current_position

        # Read the file line by line
        for line in self.f:
            line_length = len(line)
            if remaining_bytes >= line_length:
                # Decrease remaining bytes by line length
                remaining_bytes -= line_length
                lc += 1
            else:
                break

        # Restore original file position
        self.f.seek(current_position)

        if char:
            return lc, remaining_bytes
        return lc

    def close(self):
        self.f.close()

# Example usage:
file_editor = FileEditor('example.txt')
print(file_editor.tell())  # Get the line count up to the current position
file_editor.close()
