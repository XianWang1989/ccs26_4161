
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        lc, t = 0, current_position
        self.f.seek(0)

        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(current_position)
        if char:
            return lc, t
        return lc

# Example usage
editor = FileEditor('example.txt')
line_number = editor.tell()
print(f"Current line number: {line_number}")
editor.f.close()
