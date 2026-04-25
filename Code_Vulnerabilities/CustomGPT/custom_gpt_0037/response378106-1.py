
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)

        # Read all lines into memory (avoid lazy iteration)
        lines = self.f.readlines()
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the previous position
        self.f.seek(t + sum(len(lines[i]) for i in range(lc)))

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
# Now you can safely use the tell method
line_count = file_editor.tell()
print(f"Current line position: {line_count}")
file_editor.close()
