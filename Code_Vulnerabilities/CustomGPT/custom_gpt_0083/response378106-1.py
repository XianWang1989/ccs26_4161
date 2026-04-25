
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()

        # Move to the beginning to read all lines
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # Line count

        # Determine line and character position
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the previous file position
        self.f.seek(t)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get line count
editor.close()
