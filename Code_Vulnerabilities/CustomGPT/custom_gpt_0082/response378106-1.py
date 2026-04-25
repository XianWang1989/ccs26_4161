
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save current position and seek to the beginning
        t = self.f.tell()
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()
        self.f.seek(t)  # Restore original position

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

    def close(self):
        self.f.close()
