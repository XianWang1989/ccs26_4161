
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current file position
        self.f.seek(0)  # Move to the beginning of the file
        lines = self.f.readlines()  # Read all lines into a list
        self.f.seek(t)  # Restore the original file position

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def __del__(self):
        self.f.close()  # Ensure the file is closed when done
