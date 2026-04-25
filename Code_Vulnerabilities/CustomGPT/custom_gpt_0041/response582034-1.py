
class MyForIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        except StopIteration:
            self.exit_loop()
            raise
        finally:
            self.loop_end()

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

def my_for(loop_iterable):
    return MyForIterator(loop_iterable)

for i in my_for([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
