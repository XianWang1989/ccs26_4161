
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")
        self.finished = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.loop_iterable)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() are still executed
