
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

    def close(self):
        self.f.close()

# Example of using the FileEditor
editor = FileEditor('example.txt')
# Assume you write something before telling the position
editor.f.write("First line\nSecond line\nThird line\n")
editor.f.flush()  # Ensure the content is written

line_count = editor.tell()
print("Current line number:", line_count)

editor.close()
