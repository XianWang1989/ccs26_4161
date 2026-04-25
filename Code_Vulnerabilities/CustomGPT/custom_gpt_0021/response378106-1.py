
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)

        # Read all lines at once
        lines = self.f.readlines()
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Restore position, if needed

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
lines_count = file_editor.tell()
print(f"Number of lines before the current position: {lines_count}")
file_editor.close()
