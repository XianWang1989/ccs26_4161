
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Current byte position
        self.f.seek(0)     # Go to the start of the file
        lines = self.f.readlines()  # Read all lines into a list
        lc = 0

        # Calculate the line number based on byte position
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t + sum(len(line) for line in lines[:lc]))  # Restore the file position
        if char:
            return lc, t
        return lc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

# Example usage:
with FileEditor('example.txt') as editor:
    print(editor.tell())  # Outputs the current line number based on the byte position
