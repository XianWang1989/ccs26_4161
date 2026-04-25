
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.iterable)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop started.")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exiting the loop.")
        self.finished = True

    def __del__(self):
        if not self.finished:
            self.exit_loop()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
