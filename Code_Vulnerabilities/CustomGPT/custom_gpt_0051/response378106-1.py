
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get current position
        t = self.f.tell()

        # Read all lines into a list
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # Line counter

        # Calculate line count and relative position
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
print(editor.tell())  # Prints the current line position
editor.close()
