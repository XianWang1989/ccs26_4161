
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)
        lines = self.f.readlines()
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)
        if char:
            return lc, t
        return lc

# Usage
with FileEditor('example.txt') as editor:
    print(editor.tell())
