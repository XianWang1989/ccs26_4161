
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        original_pos = self.f.tell()
        t, lc = original_pos, 0
        self.f.seek(0)
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break
        self.f.seek(original_pos)
        if char:
            return lc, t
        return lc

# Example usage
editor = FileEditor("example_file.txt")
print(editor.tell())  # prints the line count based on the current position
