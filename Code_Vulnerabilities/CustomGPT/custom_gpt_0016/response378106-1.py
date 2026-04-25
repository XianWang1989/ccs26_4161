
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position in the file
        current_pos = self.f.tell()

        # Seek back to the beginning of the file to start counting lines
        self.f.seek(0)

        line_count = 0
        # Read through the file and count lines
        while True:
            line = self.f.readline()
            if not line:
                break
            if current_pos < len(line):
                break
            current_pos -= len(line)
            line_count += 1

        # Return either the line count or line count with position in the line
        if char:
            return line_count, current_pos
        return line_count

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('myfile.txt')
editor.f.write("First line\nSecond line\nThird line\n")
editor.f.flush()  # Ensure all data is written

# Let's check the line position
line_number = editor.tell()
print(f'Current Position is at line number: {line_number}')

editor.close()
