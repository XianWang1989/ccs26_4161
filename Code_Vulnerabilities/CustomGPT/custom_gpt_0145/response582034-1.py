
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            return next(self.iterator)
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop starting")

    def loop_end(self):
        print("Loop ending")

    def exit_loop(self):
        print("Exiting loop")

# Using the MyIterator class
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        # break will automatically cause loop_end and exit_loop to be called
        break
