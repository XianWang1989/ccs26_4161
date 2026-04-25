
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0

        self.f.seek(0)
        for line in self.f:
            line_length = len(line)
            if current_position >= line_length:
                current_position -= line_length
                line_count += 1
            else:
                break

        self.f.seek(current_position)

        if char:
            return line_count, current_position
        return line_count

    def close(self):
        self.f.close()

# Example
editor = FileEditor("example.txt")
print(editor.tell())  # Outputs line count at current position
editor.close()
