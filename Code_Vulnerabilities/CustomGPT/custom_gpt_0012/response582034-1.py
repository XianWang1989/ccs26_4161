
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.done = False
        self.enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.loop_iterable)
            return value
        except StopIteration:
            self.done = True
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop starting...")

    def loop_end(self):
        print("Loop ending...")

    def enter_loop(self):
        print("Entering loop...")

    def exit_loop(self):
        print("Exiting loop...")

    def stop(self):
        self.done = True
        self.loop_end()
        self.exit_loop()

# Usage
my_iter = MyIterator([1, 2, 3])
for i in my_iter:
    print("i:", i)
    if i == 2:
        my_iter.stop()  # This will ensure cleanup is called
        break
