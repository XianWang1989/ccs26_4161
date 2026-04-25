
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop...")

    def loop_start(self):
        print("Loop starts...")

    def loop_end(self):
        print("Loop ends...")

    def exit_loop(self):
        print("Exiting the loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            self.exit_loop()
            raise StopIteration
        try:
            self.loop_start()
            value = next(self.iterator)
            self.loop_end()
            return value
        except StopIteration:
            self.finished = True
            self.exit_loop()
            raise

# Usage example
for i in MyIterator([1, 2, 3]):
    print("i: ", i)
    if i == 2:
        break
