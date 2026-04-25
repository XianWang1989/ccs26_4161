
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_pos = self.f.tell()
        line_count = 0
        self.f.seek(0)

        for line in self.f:
            if current_pos >= len(line):
                current_pos -= len(line)
                line_count += 1
            else:
                break

        self.f.seek(current_pos)
        if char:
            return line_count, current_pos
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get line count
editor.close()
