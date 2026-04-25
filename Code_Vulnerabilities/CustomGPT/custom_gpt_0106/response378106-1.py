
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0

        # Reset the file pointer to the beginning
        self.f.seek(0)

        # Read lines and count
        while True:
            line = self.f.readline()
            if not line:  # EOF
                break
            line_count += 1
            if current_position < len(line):
                break
            current_position -= len(line)

        self.f.seek(current_position)  # Restore position

        if char:
            return line_count, current_position
        return line_count

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
print(editor.tell())  # Outputs the number of lines
editor.close()
