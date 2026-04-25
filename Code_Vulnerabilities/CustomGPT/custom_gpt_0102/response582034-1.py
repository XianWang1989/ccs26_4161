
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.loop_iterable):
            self.loop_start()
            value = self.loop_iterable[self.index]
            self.index += 1
            self.loop_end()
            return value
        else:
            self.exit_loop()
            raise StopIteration

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

# Usage of the custom iterator
for i in MyIterator([1, 2, 3]):
    print(f"i: {i}")
    if i == 2:
        break  # loop_end() and exit_loop() are called automatically
