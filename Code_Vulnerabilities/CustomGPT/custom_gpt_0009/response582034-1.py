
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.length = len(loop_iterable)

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        if self.index < self.length:
            self.loop_start()
            value = self.loop_iterable[self.index]
            self.index += 1
            self.loop_end()
            return value
        else:
            self.exit_loop()
            raise StopIteration

    def enter_loop(self):
        print("Entering Loop")

    def loop_start(self):
        print(f"Loop Start: {self.loop_iterable[self.index - 1]}")

    def loop_end(self):
        print("Loop End")

    def exit_loop(self):
        print("Exiting Loop")

# Usage
try:
    for i in MyIterator([1, 2, 3]):
        print("i: ", i)
        if i == 2:
            break  # This will invoke exit_loop() regardless of how it exits
except StopIteration:
    pass  # Gracefully handle the StopIteration exception from the iterator
