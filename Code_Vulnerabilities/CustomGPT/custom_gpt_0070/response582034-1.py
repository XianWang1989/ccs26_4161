
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Starting loop iteration")

    def loop_end(self):
        print("Ending loop iteration")

    def exit_loop(self):
        print("Exiting loop")


# Usage
for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
