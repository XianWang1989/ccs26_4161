
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.has_broken = False
        self.enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_broken:
            self.exit_loop()
            raise StopIteration
        try:
            value = next(self.iterator)
            self.loop_start()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def break_loop(self):
        self.loop_end()
        self.has_broken = True

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        MyIterator.break_loop(MyIterator([1, 2, 3]))  # Calling break_loop
        break
