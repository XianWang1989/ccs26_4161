
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self._is_running = True
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
        if not self._is_running:
            raise StopIteration
        try:
            self.loop_start()
            return next(self.loop_iterable)
        except StopIteration:
            self.exit_loop()
            raise
        finally:
            self.loop_end()

    def close(self):
        self._is_running = False
        self.exit_loop()

# Example usage
iterator = MyIterator([1, 2, 3])

try:
    for i in iterator:
        print("i:", i)
        if i == 2:
            iterator.close()  # Exit cleanly on break condition
            break
except StopIteration:
    pass
