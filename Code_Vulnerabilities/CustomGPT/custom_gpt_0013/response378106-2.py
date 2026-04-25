
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_pos = self.f.tell()
        self.f.seek(0)
        line_count = 0
        remaining = current_pos

        for line in self.f:
            if remaining >= len(line):
                remaining -= len(line)
                line_count += 1
            else:
                break

        self.f.seek(current_pos)

        if char:
            return line_count, remaining
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()  # Get the number of lines up to the current position
print(f"Lines read: {line_count}")
editor.close()
