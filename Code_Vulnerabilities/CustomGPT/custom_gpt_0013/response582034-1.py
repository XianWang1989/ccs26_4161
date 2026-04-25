
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.has_ended = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_ended:
            self.exit_loop()
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.iterable)
        except StopIteration:
            self.has_ended = True
            self.exit_loop()
            raise

        return value

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() will still be called here
