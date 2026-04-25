
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()
        # Move to the start of the file
        self.f.seek(0)
        lc = 0

        # Iterate through the file to determine line count
        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Reset the file position back to where it was
        self.f.seek(t)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()
