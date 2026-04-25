
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t, lc = self.f.tell(), 0
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Reset the cursor back to the original position

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f"Current line position: {line_count}")
editor.close()
