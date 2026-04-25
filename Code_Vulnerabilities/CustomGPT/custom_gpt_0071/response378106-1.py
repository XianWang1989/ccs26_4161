
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()  
        self.f.seek(0)  # Move to the beginning of the file

        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # Line counter
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return based on char parameter
        self.f.seek(t)  # Restore the original position
        return (lc, t) if char else lc

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell())  # Get the line count
print(editor.tell(char=True))  # Get line count and character position
editor.close()
