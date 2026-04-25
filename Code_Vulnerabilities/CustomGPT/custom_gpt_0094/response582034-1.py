
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        self.loop_start()
        try:
            value = next(self.iterator)
            return value
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def close(self):
        self.exit_loop()

# Usage
my_iter = MyIterator([1, 2, 3])
try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            my_iter.close()
            break
finally:
    my_iter.close()
