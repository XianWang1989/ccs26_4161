
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration
        item = self.loop_iterable[self.index]
        self.loop_start()
        self.index += 1
        return item

    def loop_start(self):
        print("Loop start...")

    def exit_loop(self):
        print("Exiting loop...")

    def loop_end(self):
        print("Loop end.")

    def __del__(self):
        self.exit_loop()


def my_for(loop_iterable):
    it = MyIterator(loop_iterable)
    try:
        while True:
            item = next(it)
            yield item
            it.loop_end()
    except StopIteration:
        pass


# Usage
for i in my_for([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
