
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
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
            item = next(self.iterator)
            self.loop_start()
            return item
        finally:
            self.loop_end()

    def close(self):
        self.exit_loop()

# Usage
my_iter = MyIterator([1, 2, 3])
try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break
finally:
    my_iter.close()
