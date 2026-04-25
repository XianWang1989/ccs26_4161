
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)
        lc = 0
        while True:
            line = self.f.readline()
            if not line:  # End of file
                break
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break
        self.f.seek(t)  # Reset pointer
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell())  # Get the current line number
editor.close()
