
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.started = False

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        try:
            if not self.started:
                self.started = True

            item = next(self.loop_iterable)
            self.loop_start()
            return item
        except StopIteration:
            self.exit_loop()
            raise

    def __del__(self):
        if self.started:
            self.exit_loop()


# Using the custom iterator
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
