
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Loop starting.")

    def loop_end(self):
        print("Loop ending.")

    def exit_loop(self):
        print("Exiting the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            self.exit_loop()
            raise StopIteration

        self.loop_start()
        value = self.iterable[self.index]
        self.index += 1
        self.loop_end()
        return value

    def close(self):
        self.exit_loop()

# Using the iterator
my_iter = MyIterator([1, 2, 3])
try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break
except StopIteration:
    pass
finally:
    my_iter.close()
