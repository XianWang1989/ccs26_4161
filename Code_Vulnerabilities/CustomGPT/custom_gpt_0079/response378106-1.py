
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        line_count = 0

        # Store the current position to restore it later
        current_position = self.f.tell()
        self.f.seek(0)

        for line in self.f:
            if t >= len(line):
                t -= len(line)
                line_count += 1
            else:
                break

        # Restore the original position in the file
        self.f.seek(current_position)

        if char:
            return line_count, t
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Output: number of lines
editor.close()
