
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.is_finished = False
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_finished:
            exit_loop()
            raise StopIteration

        loop_start()
        try:
            item = next(self.iterator)
            return item
        except StopIteration:
            self.is_finished = True
            exit_loop()
            raise
        finally:
            loop_end()

def enter_loop():
    print("Entered loop.")

def loop_start():
    print("Loop start.")

def loop_end():
    print("Loop end.")

def exit_loop():
    print("Exited loop.")

# Using the MyIterator class
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
