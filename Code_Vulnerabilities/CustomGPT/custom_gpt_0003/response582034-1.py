
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable

    def __enter__(self):
        self.enter_loop()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_loop()
        return False  # Propagate any exceptions (like KeyboardInterrupt, etc.)

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        for i in self.loop_iterable:
            self.loop_start()
            yield i
            self.loop_end()


# Using the custom iterator with a context manager
with MyIterator([1, 2, 3]) as my_iter:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break  # This will trigger the exit procedure
