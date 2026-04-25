
class MyForIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def exit_loop(self):
        print("Exiting loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            item = next(self.iterator)
            self.loop_end()
            return item
        except StopIteration:
            self.exit_loop()
            raise

# Using the custom iterator
for i in MyForIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
