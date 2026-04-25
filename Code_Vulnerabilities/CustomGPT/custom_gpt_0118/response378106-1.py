
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Current position
        lc = 0  # Line count
        self.f.seek(0)  # Move to the start

        # Read the file content and count lines
        while True:
            line = self.f.readline()  # Read line by line
            if not line:  # End of file
                break
            if t >= len(line):
                t -= len(line)  # Reduce the offset
                lc += 1  # Increment line count
            else:
                break

        self.f.seek(t)  # Restore the original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()
