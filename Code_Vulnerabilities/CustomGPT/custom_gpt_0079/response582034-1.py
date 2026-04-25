
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.loop_iterable)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def close(self):
        self.loop_end()
        self.exit_loop()


# Usage
my_iter = MyIterator([1, 2, 3])
for i in my_iter:
    print(f"i: {i}")
    if i == 2:
        my_iter.close()  # Ensure cleanup on exit
        break
