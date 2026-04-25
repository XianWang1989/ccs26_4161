
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()
        lc = 0

        # Store the current position
        current_position = self.f.tell()

        self.f.seek(0)  # Go to the start to read lines
        for line in self.f:
            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        # Restore the original position
        self.f.seek(current_position)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Total lines: {line_count}')
editor.close()
