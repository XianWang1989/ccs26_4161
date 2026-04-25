
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Current position
        self.f.seek(0)

        lines = self.f.readlines()  # Read all lines into memory
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Reset file pointer back to original position
        self.f.seek(t + sum(len(lines[i]) for i in range(lc)))

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    print(editor.tell())  # Get the line and character index
