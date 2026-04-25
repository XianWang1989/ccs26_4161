
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        self.loop_start()
        try:
            value = next(self.iterator)
        except StopIteration:
            self.exit_loop()
            raise
        self.loop_end()
        return value

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Starting iteration")

    def loop_end(self):
        print("Ending iteration")

    def exit_loop(self):
        print("Exiting loop")


# Usage example
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
