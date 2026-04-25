
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterator = iter(loop_iterable)
        self.has_started = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_started:
            self.enter_loop()
            self.has_started = True

        self.loop_start()
        try:
            value = next(self.iterator)
        except StopIteration:
            self.exit_loop()
            raise

        self.loop_end()
        return value

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")

# Example usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
