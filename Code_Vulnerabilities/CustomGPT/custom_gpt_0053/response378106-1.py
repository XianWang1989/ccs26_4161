
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()

        # Read all lines at once and track line and character positions
        self.f.seek(0)
        lines = self.f.readlines()

        line_count = 0
        char_count = 0

        for line in lines:
            if char_count + len(line) > current_position:
                break
            char_count += len(line)
            line_count += 1

        # Return either line count or both line and character count
        if char:
            return line_count, current_position - char_count
        return line_count

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
print(file_editor.tell())  # Outputs the current line number
file_editor.close()
