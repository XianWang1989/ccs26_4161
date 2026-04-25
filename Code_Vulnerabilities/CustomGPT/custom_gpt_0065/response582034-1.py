
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iter = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entered loop.")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.iter)
            self.loop_start()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exited loop.")

    def __del__(self):
        self.exit_loop()  # Ensure cleanup

for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
