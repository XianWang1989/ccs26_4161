
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.has_exited = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_exited:
            raise StopIteration
        try:
            self.loop_start()
            item = next(self.loop_iterable)
            return item
        except StopIteration:
            self.exit_loop()
            self.has_exited = True
            raise

    def loop_start(self):
        print("Loop starting.")

    def loop_end(self):
        print("Loop ending.")

    def exit_loop(self):
        print("Exiting loop.")

    def close(self):
        self.exit_loop()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
