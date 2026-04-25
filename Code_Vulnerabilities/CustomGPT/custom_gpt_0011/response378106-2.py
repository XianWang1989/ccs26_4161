
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0
        self.f.seek(0)

        try:
            for line in self.f:
                if current_position >= len(line):
                    current_position -= len(line)
                    line_count += 1
                else:
                    break
        finally:
            self.f.seek(current_position)

        if char:
            return line_count, current_position
        return line_count

# Example usage
editor = FileEditor('example.txt')
line_number = editor.tell()
print(f'Current line number: {line_number}')
