
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
        if self.index < len(self.loop_iterable):
            loop_start()
            value = self.loop_iterable[self.index]
            self.index += 1
            loop_end()
            return value
        else:
            self.exit_loop()
            raise StopIteration()

    def loop_start(self):
        print(f"Loop start: {self.loop_iterable[self.index - 1]}")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")


# Usage of MyIterator
try:
    for i in MyIterator([1, 2, 3]):
        print("i:", i)
        if i == 2:
            raise StopIteration  # This triggers cleanup
except StopIteration:
    pass
