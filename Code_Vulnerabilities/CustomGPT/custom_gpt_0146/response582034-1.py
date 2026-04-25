
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.is_exited = False
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_exited:
            raise StopIteration
        try:
            loop_start()
            value = next(self.loop_iterable)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_end(self):
        print("End of loop processing.")

    def exit_loop(self):
        print("Exiting loop processing.")
        self.is_exited = True

    def __del__(self):
        if not self.is_exited:  # If the loop has not exited yet
            self.exit_loop()


def enter_loop():
    print("Entering loop.")

def loop_start():
    print("Start of loop processing.")


for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
