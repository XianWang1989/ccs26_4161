
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iter = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_item = next(self.iter)
        except StopIteration:
            self.exit_loop()
            raise

        self.loop_start()
        return next_item

    def __del__(self):
        self.exit_loop()  # Ensure exit is called if the object is deleted.

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() will still be called
