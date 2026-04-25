
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store all lines in memory
        self.f.seek(0)  # Ensure we're at the start of the file
        lines = self.f.readlines()

        # Get current position
        t = self.f.tell()
        lc = 0

        # Calculate line count based on byte position
        for line in lines:
            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Usage example
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Number of lines: {line_count}")
editor.close()
