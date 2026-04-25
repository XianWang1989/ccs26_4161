
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.loop_iterable):
            self.loop_start()
            value = self.loop_iterable[self.index]
            self.index += 1
            return value
        else:
            self.exit_loop()
            raise StopIteration  # End of iteration

    def loop_start(self):
        print(f"Loop start for index {self.index}")

    def loop_end(self):
        print(f"Loop end for index {self.index - 1}")

    def exit_loop(self):
        print("Exiting loop.")

    def __del__(self):
        self.exit_loop()  # Ensure cleanup on object deletion

# Example usage:
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Cleanup occurs automatically
