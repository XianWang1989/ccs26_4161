
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)

        line_count = 0
        current_position = 0

        for line in self.f:
            line_length = len(line)
            if current_position + line_length > t:
                break
            current_position += line_length
            line_count += 1

        self.f.seek(t)  # Reset to original position

        if char:
            return line_count, t - current_position
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_num = editor.tell()
print(f"Number of lines before the current position: {line_num}")
editor.close()
