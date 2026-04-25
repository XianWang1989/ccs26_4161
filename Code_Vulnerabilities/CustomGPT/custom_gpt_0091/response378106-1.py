
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()
        line_count = 0
        char_position = 0

        # Seek to the beginning to read the file
        self.f.seek(0)
        while True:
            line = self.f.readline()  # Read line by line
            if not line:  # End of file
                break

            # Increment line count
            line_count += 1

            # If current position is within the line length
            if char_position + len(line) > current_position:
                # Calculate the character position in the line
                char_position = current_position - char_position
                break

            # Update character position
            char_position += len(line)

        # Restore the original position
        self.f.seek(current_position)

        # Return results based on char flag
        if char:
            return line_count, char_position
        return line_count

    def close(self):
        self.f.close()
