
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            loop_start()
            return next(self.loop_iterable)
        finally:
            loop_end()

    def close(self):
        exit_loop()

# Here are the function definitions for entering and exiting the loop
def enter_loop():
    print("Entering loop...")

def loop_start():
    print("Starting new iteration...")

def loop_end():
    print("Ending iteration...")

def exit_loop():
    print("Exiting loop...")

# Now you can create an instance of the custom iterator
iterator = CustomIterator([1, 2, 3])
try:
    for i in iterator:
        print("i:", i)
        if i == 2:
            break
finally:
    iterator.close()
