
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop!")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop started.")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exiting the loop!")

    def close(self):
        self.exit_loop()


# Use the custom iterator
my_iter = MyIterator([1, 2, 3])
try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break  # Loop will exit and cleanup will happen
finally:
    my_iter.close()  # Ensure exit loop code runs
