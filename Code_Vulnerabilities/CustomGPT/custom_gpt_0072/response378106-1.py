
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        lc = 0
        # Save the current position
        current_pos = self.f.tell()

        # Move to the beginning of the file
        self.f.seek(0)

        try:
            for line in self.f:
                if t >= len(line):
                    t -= len(line)
                    lc += 1
                else:
                    break
        finally:
            # Restore the original position
            self.f.seek(current_pos)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Usage example
if __name__ == "__main__":
    editor = FileEditor('example.txt')
    # Add content to the file as needed
    line_count = editor.tell()
    print(f'Line count: {line_count}')
    editor.close()
