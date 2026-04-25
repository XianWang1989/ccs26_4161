
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current position
        lc = 0
        self.f.seek(0)  # Go back to the start of the file
        lines = self.f.readlines()  # Read all lines at once

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example of using the FileEditor class
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Total lines: {line_count}')
editor.close()
