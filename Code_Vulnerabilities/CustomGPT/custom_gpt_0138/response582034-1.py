
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration
        item = self.loop_iterable[self.index]
        self.loop_start()
        self.index += 1
        return item

    def loop_start(self):
        print(f"Starting loop with i: {self.loop_iterable[self.index - 1]}")

    def loop_end(self):
        print(f"Ending loop with i: {self.loop_iterable[self.index - 1]}")

    def exit_loop(self):
        print("Exiting loop")

    def __del__(self):
        if self.index < len(self.loop_iterable):  # Ensure exit_loop is called if loop was interrupted
            self.exit_loop()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
