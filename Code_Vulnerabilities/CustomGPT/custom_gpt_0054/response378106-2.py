
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t, lc = self.f.tell(), 0
        self.f.seek(0)
        lines = self.f.readlines()
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
editor = FileEditor("example.txt")
# Assuming "example.txt" has some content
current_line = editor.tell()  # Get the current line number
print("Current line:", current_line)
editor.close()
