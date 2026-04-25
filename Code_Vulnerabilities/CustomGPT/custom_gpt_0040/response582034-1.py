
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration

        i = self.loop_iterable[self.index]
        self.loop_start()
        self.index += 1
        return i

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting the loop.")

    def close(self):
        self.loop_end()
        self.exit_loop()

# Example usage
my_iter = MyIterator([1, 2, 3])

try:
    for i in my_iter:
        print("i:", i)
        if i == 2:
            break
        my_iter.loop_end()  # This is called automatically, but if you want to do something special, you can call it here.
except StopIteration:
    pass
finally:
    my_iter.close()  # Ensure closure and final cleanup.
