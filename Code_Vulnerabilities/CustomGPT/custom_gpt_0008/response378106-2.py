
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_pos = self.f.tell()
        self.f.seek(0)
        lc = 0

        for line in self.f:
            if current_pos >= len(line):
                current_pos -= len(line)
                lc += 1
            else:
                break

        self.f.seek(current_pos)

        if char:
            return lc, current_pos
        return lc

# Usage
editor = FileEditor("example.txt")
line_count = editor.tell()
print(f"Current line count: {line_count}")
