
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        t = self.f.tell()
        # Move the pointer to the start without changing the file mode
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # Line counter
        remaining = t  # Remaining bytes

        for line in lines:
            if remaining >= len(line):
                remaining -= len(line)
                lc += 1
            else:
                break

        # Restore the pointer position
        self.f.seek(t)

        if char:
            return lc, remaining
        return lc

    def close(self):
        self.f.close()

# Usage example
with FileEditor('example.txt') as editor:
    line_count = editor.tell()
    print(f'Current line: {line_count}')
