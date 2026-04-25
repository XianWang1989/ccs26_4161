
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        t = self.f.tell()

        # Move to the beginning of the file to read lines
        self.f.seek(0)

        lc = 0  # Line counter
        # Read through the file line by line
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Restore the original position
        self.f.seek(t + sum(len(line) for line in self.f))

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell())  # Output the line count or line position
editor.close()
