
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration

        self.loop_start()
        value = self.loop_iterable[self.index]
        self.index += 1
        self.loop_end()
        return value

# Usage:
iterator = MyIterator([1, 2, 3])
for i in iterator:
    print("i:", i)
    if i == 2:
        break  # Cleanup will happen automatically.
