
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            return next(self.iterator)
        except StopIteration:
            self.exit_loop()
            raise
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")

# Using the custom iterator
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
