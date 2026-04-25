
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def loop_start(self):
        print("Loop starting")

    def loop_end(self):
        print("Loop ending")

    def exit_loop(self):
        print("Exiting the loop")
        self.finished = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration

        loop_start()

        try:
            value = next(self.loop_iterable)
        except StopIteration:
            self.exit_loop()
            raise

        loop_end()
        return value

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
