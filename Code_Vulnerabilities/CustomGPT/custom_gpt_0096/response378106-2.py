
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0
        remaining = current_position
        self.f.seek(0)

        for line in self.f:
            line_length = len(line)
            if remaining >= line_length:
                remaining -= line_length
                line_count += 1
            else:
                break

        self.f.seek(current_position)

        if char:
            return line_count, remaining
        return line_count

# Usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Number of lines up to current position: {line_count}')
