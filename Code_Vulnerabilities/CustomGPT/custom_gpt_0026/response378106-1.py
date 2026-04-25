
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current file position
        t = self.f.tell()
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return character info if requested
        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()

# Usage example
editor = FileEditor('example.txt')
editor.f.write("Line 1\nLine 2\nLine 3\n")
editor.f.flush()  # Ensures all data is written

line_count = editor.tell()
print(f'Total lines: {line_count}')
