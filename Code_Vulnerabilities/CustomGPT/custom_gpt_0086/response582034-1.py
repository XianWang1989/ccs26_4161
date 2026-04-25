
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.is_finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_finished:
            self.exit_loop()
            raise StopIteration

        try:
            item = next(self.loop_iterable)
            self.loop_start()
            return item
        except StopIteration:
            self.is_finished = True
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

# Using the custom iterator
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
