
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # get the current position
        self.f.seek(0)     # go back to the start
        lc = 0             # line count

        # Read lines without moving the cursor unexpectedly
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break
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
line_count = editor.tell()
print(f'Line count: {line_count}')
editor.close()
