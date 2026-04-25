
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.running = True
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.running:
            exit_loop()
            raise StopIteration

        try:
            loop_start()
            value = next(self.iterator)
            return value
        except StopIteration:
            exit_loop()
            raise
        finally:
            loop_end()

def enter_loop():
    print("Entering loop...")

def loop_start():
    print("Loop started.")

def loop_end():
    print("Loop ended.")

def exit_loop():
    print("Exiting loop...")

for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
