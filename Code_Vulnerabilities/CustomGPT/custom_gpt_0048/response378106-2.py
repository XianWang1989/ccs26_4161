
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)
        lines = self.f.readlines()
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break
        self.f.seek(t)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example of usage
with FileEditor('example.txt') as editor:
    # Write some lines to file for demonstration
    editor.f.write("Line 1\nLine 2\nLine 3\n")
    editor.f.flush()  # Flush to ensure data is written

    # Get line and character position
    line_col = editor.tell(char=True)
    print(line_col)  # Output: (line number, character offset)
