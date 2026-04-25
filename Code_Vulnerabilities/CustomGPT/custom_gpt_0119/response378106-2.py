
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # (implementation as shown above)

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
line, char = editor.tell(char=True)  # Get line count and character position
print(f"Line: {line}, Character Position: {char}")
editor.close()
