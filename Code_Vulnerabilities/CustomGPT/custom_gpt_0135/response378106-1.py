
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()

        # Read all lines into a list
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # line count
        t = current_position  # relative position in the current line

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
