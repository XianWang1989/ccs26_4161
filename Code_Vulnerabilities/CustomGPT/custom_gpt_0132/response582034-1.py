
class CustomIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.loop_start()
            value = self.iterable[self.index]
            self.index += 1
            self.loop_end()
            return value
        else:
            self.exit_loop()
            raise StopIteration

    def loop_start(self):
        print(f"Loop start for iteration {self.index}")

    def loop_end(self):
        print(f"Loop end for iteration {self.index}")

    def exit_loop(self):
        print("Exiting the loop")

# Usage example
for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # This will trigger cleanup before exiting
