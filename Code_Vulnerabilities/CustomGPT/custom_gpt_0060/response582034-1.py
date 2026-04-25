
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.is_exiting = False
        self.enter_loop()

    def enter_loop(self):
        print("Entered loop")

    def loop_start(self):
        print("Loop started")

    def loop_end(self):
        print("Loop ended")

    def exit_loop(self):
        print("Exited loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_exiting:
            self.exit_loop()
            raise StopIteration

        try:
            value = next(self.iterator)
            self.loop_start()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def stop(self):
        self.is_exiting = True

# Usage of the custom iterator
my_iterable = MyIterator([1, 2, 3])
for i in my_iterable:
    print("i:", i)
    if i == 2:
        my_iterable.stop()  # Call `stop` method instead of break
        break
