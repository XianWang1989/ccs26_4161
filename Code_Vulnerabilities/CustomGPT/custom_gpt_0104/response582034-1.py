
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.started = False

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        self.enter_loop()
        self.started = True
        return self

    def __next__(self):
        if not self.started:
            self.enter_loop()

        try:
            item = next(self.iterator)
            self.loop_start()
            return item
        except StopIteration:
            self.exit_loop()
            raise

    def close(self):
        if self.started:
            self.loop_end()
            self.exit_loop()

# Usage:
my_iter = MyIterator([1, 2, 3])
try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            my_iter.close()  # Call close to ensure cleanup
            break
finally:
    my_iter.close()  # Ensure we call close when iteration is complete
