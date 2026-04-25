
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)
        lines = self.f.readlines()  # Read all lines at once
        lc = 0
        remaining_t = t  # Track the remaining offset

        for line in lines:
            if remaining_t >= len(line):
                remaining_t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Reset the file cursor to the original position

        if char:
            return lc, remaining_t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell(char=True))
editor.close()
