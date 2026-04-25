
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()
        self.f.seek(0)  # Go to the start of the file

        # Read all lines into memory
        lines = self.f.readlines()
        lc = 0  # Line count

        # Calculate current line and position in the line
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Check if character count is needed
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Usage example
editor = FileEditor('example.txt')
line_number = editor.tell()
print(f'Current line: {line_number}')
editor.close()
