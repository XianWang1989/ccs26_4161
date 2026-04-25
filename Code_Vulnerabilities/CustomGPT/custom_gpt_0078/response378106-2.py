
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        self.f.seek(0)
        lines = self.f.readlines()
        t = self.f.tell()

        lc = 0
        current_pos = 0

        for line in lines:
            if current_pos + len(line) > t:
                break
            current_pos += len(line)
            lc += 1

        if char:
            return lc, t
        return lc

# Example usage
editor = FileEditor("example.txt")
print(editor.tell())
