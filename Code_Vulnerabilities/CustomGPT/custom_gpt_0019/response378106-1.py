
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        self.f.seek(0)

        # Read all lines into a list to avoid modifying the iterator
        lines = self.f.readlines()
        lc = 0
        t = current_position

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(current_position)  # Restore cursor position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Current line count: {line_count}")
editor.close()
