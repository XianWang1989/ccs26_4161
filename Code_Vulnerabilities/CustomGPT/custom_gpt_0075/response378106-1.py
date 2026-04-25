
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')
        self.lines = self.read_lines()

    def read_lines(self):
        self.f.seek(0)  # Go to the beginning of the file
        return self.f.readlines()

    def tell(self, char=False):
        pos = self.f.tell()
        line_count = 0

        for line in self.lines:
            if pos >= len(line):
                pos -= len(line)
                line_count += 1
            else:
                break

        if char:
            return line_count, pos
        return line_count

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
line_number = editor.tell()  # Get line number
print(f'Current line number: {line_number}')
editor.close()
