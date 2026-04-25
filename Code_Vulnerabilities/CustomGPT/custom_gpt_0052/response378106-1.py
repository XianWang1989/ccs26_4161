
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        t = self.f.tell()
        # Move to the beginning of the file
        self.f.seek(0)

        lc = 0  # Line count
        # Read lines until reaching the position
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore pointer position
        self.f.seek(t)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    print(editor.tell())
