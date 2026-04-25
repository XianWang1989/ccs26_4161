
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get current position
        self.f.seek(0)     # Move to the start of the file

        lc = 0
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break
            if t >= len(line):  # Check if current position exceeds line length
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Restore the original position

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()
