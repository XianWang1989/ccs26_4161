
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        lc = 0
        self.f.seek(0)

        while True:
            line = self.f.readline()
            if not line:
                break
            line_length = len(line)
            if t >= line_length:
                t -= line_length
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
editor.f.write('Hello\nWorld\nThis is a test.\n')
editor.f.seek(0)  # Move cursor to the beginning to test the tell function
print(editor.tell())  # Output should represent the line count at the current position
editor.close()
