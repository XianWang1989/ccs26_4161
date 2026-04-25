
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()

        # Read all lines into memory
        self.f.seek(0)  # Go to the beginning of the file
        lines = self.f.readlines()

        # Now determine the line count and character offset
        line_count = 0
        line_offset = current_position

        for line in lines:
            if line_offset >= len(line):
                line_offset -= len(line)
                line_count += 1
            else:
                break

        # Restore the pointer to its original position
        self.f.seek(current_position)

        if char:
            return line_count, line_offset
        return line_count

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
line_num = file_editor.tell()
print(f"Current line number: {line_num}")
file_editor.close()
