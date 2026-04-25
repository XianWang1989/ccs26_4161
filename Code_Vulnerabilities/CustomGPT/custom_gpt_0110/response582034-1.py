
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self._entered = False

    def __iter__(self):
        self.enter_loop()
        self._entered = True
        return self

    def __next__(self):
        try:
            self.loop_start()
            return next(self.loop_iterable)
        except StopIteration:
            self.exit_loop()
            raise

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        if self._entered:
            print("Exiting loop")

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
