
class LineBasedFile:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')
        # Read all lines into memory
        self.f.seek(0)
        self.lines = self.f.readlines()

    def tell(self, char=False):
        # Gets current position
        t = self.f.tell()
        lc = 0

        # Iterate over lines to compute their lengths
        for line in self.lines:
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
file_handler = LineBasedFile('example.txt')
print(file_handler.tell())  # Returns the current line number
file_handler.close()
