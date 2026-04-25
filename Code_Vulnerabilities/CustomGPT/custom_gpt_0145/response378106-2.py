
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        original_position = self.f.tell()
        self.f.seek(0)
        t, lc = original_position, 0
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break
        self.f.seek(original_position)
        if char:
            return lc, t
        return lc

# Example usage:
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Line count: {line_count}")
editor.f.close()
