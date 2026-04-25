
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iter = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iter)
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
my_iterator = MyFor([1, 2, 3])
try:
    for i in my_iterator:
        print("i:", i)
        if i == 2:
            break
finally:
    my_iterator.close()
