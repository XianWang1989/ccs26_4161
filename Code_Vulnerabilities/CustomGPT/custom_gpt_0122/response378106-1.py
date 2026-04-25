
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Read all lines into memory
        self.f.seek(0)  # Go to the beginning
        lines = self.f.readlines()

        # Get the current byte position
        t = self.f.tell()
        lc = 0  # Line count

        # Calculate which line and character position
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

# Example usage
editor = FileEditor('example.txt')
editor.f.write("First line\nSecond line\nThird line\n")
editor.f.flush()  # Make sure to flush before trying to tell
print(editor.tell())  # Output the current line count
editor.close()
