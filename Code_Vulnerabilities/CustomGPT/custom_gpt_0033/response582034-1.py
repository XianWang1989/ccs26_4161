
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.active = True
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        if not self.active:
            raise StopIteration
        try:
            self.loop_start()
            value = next(self.iterable)
            return value
        except StopIteration:
            self.exit_loop()
            self.active = False
            raise

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def close(self):
        if self.active:
            self.loop_end()
            self.exit_loop()


# Usage of MyIterator
iterator = MyIterator([1, 2, 3])
try:
    for i in iterator:
        print("i:", i)
        if i == 2:
            break  # This will trigger cleanup automatically
finally:
    iterator.close()  # Ensure cleanup even if not called in loop
