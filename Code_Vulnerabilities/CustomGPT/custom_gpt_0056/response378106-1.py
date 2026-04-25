
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        # Store the current position
        self.f.seek(0)
        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the cursor position
        self.f.seek(t + len(lines[lc - 1]) if lc > 0 else 0)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'Current line position: {line_count}')
editor.close()
