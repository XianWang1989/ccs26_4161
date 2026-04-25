
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()

        # Seek to the beginning of the file and read all lines
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)
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
lines_count = editor.tell()
print(f"Number of lines: {lines_count}")
editor.close()
