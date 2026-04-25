
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterable = iter(loop_iterable)
        self.is_finished = False

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        if self.is_finished:
            raise StopIteration
        try:
            self.loop_start()
            value = next(self.iterable)
            return value
        finally:
            self.loop_end()

    def finish(self):
        self.exit_loop()
        self.is_finished = True

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        # Cleanup and exit the loop
        MyIterator.finish(MyIterator)
        break
