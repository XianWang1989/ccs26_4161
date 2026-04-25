
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)
        lines = self.f.readlines()  # Read all lines into a list
        lc = 0

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Return to the original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell())  # This will print the line count
editor.close()
