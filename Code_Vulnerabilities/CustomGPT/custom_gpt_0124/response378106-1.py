
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()  # Get current position
        self.f.seek(0)  # Go to the start of the file

        # Read all lines at once
        lines = self.f.readlines()
        lc = 0  # Line count

        # Calculate line number and character offset
        for line in lines:
            if current_position >= len(line):
                current_position -= len(line)
                lc += 1
            else:
                break

        self.f.seek(current_position)  # Reset position after reading
        if char:
            return lc, current_position
        return lc

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
line_number = editor.tell()
print(f"Current line number: {line_number}")
editor.close()
