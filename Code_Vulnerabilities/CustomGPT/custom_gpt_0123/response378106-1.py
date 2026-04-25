
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        t = self.f.tell()
        lc = 0

        # Seek to the beginning of the file
        self.f.seek(0)

        # Read lines while keeping track of position
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return based on the char flag
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Current line count: {line_count}")
editor.close()
