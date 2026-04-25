
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)

    def __enter__(self):
        self.enter_loop()
        return self

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def enter_loop(self):
        print("Entering loop")

    def exit_loop(self):
        print("Exiting loop")

# Usage
with MyIterator([1, 2, 3]) as my_iter:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break
