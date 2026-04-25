
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store current position
        t = self.f.tell()
        lc = 0

        # Move the pointer to the beginning
        self.f.seek(0)

        # Iterate over the lines
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break

            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return the line count and the character position if needed
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Current line position: {line_count}')
editor.close()
