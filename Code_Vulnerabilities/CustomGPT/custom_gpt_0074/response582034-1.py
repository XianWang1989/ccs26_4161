
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.is_running = True
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.is_running:
            exit_loop()
            raise StopIteration

        try:
            loop_start()
            value = next(self.loop_iterable)
            return value
        except StopIteration:
            exit_loop()
            self.is_running = False
            raise

    def end(self):
        if self.is_running:
            loop_end()

    def __del__(self):
        if self.is_running:
            exit_loop()

def enter_loop():
    print("Entering loop.")

def loop_start():
    print("Loop starting.")

def loop_end():
    print("Loop ending.")

def exit_loop():
    print("Exiting loop.")

# Using the custom iterator
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
    # Call end on every iteration to ensure loop_end() is executed
    MyFor.end()
